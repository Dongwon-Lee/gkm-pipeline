# Import motif_database snakefile
module motif_database:
    snakefile: 'motif_database.smk'
    config: config

# Import kmers snakefile
module kmers:
    snakefile: 'kmers.smk'
    config: config

use rule * from motif_database as motif_database_* 
use rule * from kmers as kmers_* 

# Default rule which runs all motif enrichment analysis steps
rule all:
    default_target: True
    input:
        expand("results/{sample}/{sample}.{word_length}mers.all_tfs.txt", word_length=config["word_length"], sample=config["samples"]),
        expand("results/{sample}/{sample}.{word_length}mers.expr_enriched_tfs.html", word_length=config["word_length"], sample=config["samples"])

# If qc cleaning was not already performed, clean the input bed file to remove irrelevant information
rule clean_bed:
    output:
        "results/samples/bed/{sample}.clean.bed"
    params:
        word_length = config['word_length']
    shell:
        """
        QC_OUT=results/qc/{wildcards.sample}.{params.word_length}mers.gkmqc/{wildcards.sample}.{params.word_length}mers.e300.qc.bed
        BASE_BED=data/samples/{wildcards.sample}.bed
        if [ -f "$QC_OUT" ]; then
            cp "$QC_OUT" {output}
        else 
            grep -v 'chrUn\|chrM\|random' "$BASE_BED" > {output}
        fi
        """

# Generate negative dataset for model training
rule generate_null_seq:
    input:
        "results/samples/bed/{sample}.clean.bed"
    output:
        neg_bed = "results/samples/bed/{sample}.neg.bed",
        neg_fa = "results/samples/fasta/{sample}.neg.fa",
        fa = "results/samples/fasta/{sample}.fa"
    params:
        gkmQC_path = config['paths']['gkmQC']
    threads: 10
    shell:
        "python -E {params.gkmQC_path}/scripts/seqs_nullgen.py -p {input} -n {output.neg_bed} -g hg38 -@ {threads} && "
        "mv results/samples/bed/{wildcards.sample}.neg.fa {output.neg_fa} && "
        "mv results/samples/bed/{wildcards.sample}.clean.fa {output.fa}"

# Returns number of threads to use for model training
def get_num_threads(wildcards):
    return 16 if workflow.cores >= 16 else 4 if workflow.cores < 16 and workflow.cores >= 4 else 1

# Returns -d flag (number of mismatches) value to use for training
def get_d(wildcards):
    return int(wildcards.word_length) - 7 if int(wildcards.word_length) <= 9 else 3

# Run LS-GKM model training step 
rule gkm_train:
    input:
        pos = "results/samples/fasta/{sample}.fa",
        neg = "results/samples/fasta/{sample}.neg.fa"
    output:
        "results/models/{sample}.{word_length}mers.model.txt"
    params:
        lsgkm_path = config['paths']['lsgkm'],
        d = get_d
    threads: get_num_threads
    resources:
        mem_mb = lambda wildcards, input: max(input.size_mb * 512, 512)
    shell:
        "{params.lsgkm_path}/bin/gkmtrain -l {wildcards.word_length} -d {params.d} -m {resources.mem_mb} -T {threads} {input.pos} {input.neg} results/models/{wildcards.sample}.{wildcards.word_length}mers"

# Run LS-GKM model prediction step (against all k-mers)
rule gkm_predict:
    input:
        kmers = rules.kmers_get_kmers.output,
        model = "results/models/{sample}.{word_length}mers.model.txt"
    output:
        "results/weights/{sample}.{word_length}mers.svmw.txt"
    params:
        lsgkm_path = config['paths']['lsgkm']
    threads: get_num_threads
    shell:
        "{params.lsgkm_path}/bin/gkmpredict -T {threads} {input.kmers} {input.model} {output}"

# Run scripts/count_kmers_per_motif.py script to perform motif enrichment analysis on model predictions
rule enriched_tfs:
    input:
        "results/weights/{sample}.{word_length}mers.svmw.txt",
        rules.motif_database_all.input
    output:
        "results/{sample}/{sample}.{word_length}mers.all_tfs.txt",
        "results/{sample}/{sample}.{word_length}mers.expr_enriched_tfs.html"
    params:
        tf_metadata_file = config['tf_metadata_file'],
        percentile_cutoff = config['enrichment_thresholds']['percentile_cutoff'],
        enrichment_score = config['enrichment_thresholds']['enrichment_score'],
        padj_cutoff_poisson = config['enrichment_thresholds']['padj_cutoff_poisson'],
        padj_cutoff_wilcox = config['enrichment_thresholds']['padj_cutoff_wilcox']
    shell:
        "python -E workflow/scripts/count_kmers_per_motif.py {input} results/{wildcards.sample}/{wildcards.sample}.{wildcards.word_length}mers "
        "{params.percentile_cutoff} {params.enrichment_score} {params.padj_cutoff_poisson} {params.padj_cutoff_wilcox} data/tf_database/{params.tf_metadata_file}.txt"