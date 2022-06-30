rule all:
    default_target: True
    input:
        expand("results/{sample}/{sample}.{word_length}mers.gkmqc.curve.pdf", sample=config["samples"], word_length=config["word_length"])

rule qc_eval:
    input:
        "data/samples/{sample}.bed"
    output:
        directory("data/samples/{sample}.{word_length}mers.gkmqc/")
    threads: 10
    params:
        gkmQC_path = config['paths']['gkmQC'],
        score_col = config['bed_score_col']
    resources:
        mem_mb = lambda wildcards, input: max(input.size_mb * 512, 512)
    shell:
        "cd data/samples && "
        "python -E {params.gkmQC_path}/bin/gkmqc.py evaluate -i {wildcards.sample}.bed -g hg38 "
        "-n {wildcards.sample}.{wildcards.word_length}mers -o {params.score_col} "
        "-@ {threads} -L {wildcards.word_length} -c {resources.mem_mb}"

rule move_qc_output:
    input:
        rules.qc_eval.output
    output:
        eval_out = "results/qc/{sample}.{word_length}mers.gkmqc/{sample}.{word_length}mers.gkmqc.eval.out",
        full_bed_out = "results/qc/{sample}.{word_length}mers.gkmqc/{sample}.{word_length}mers.e300.qc.bed"
    shell:
        "mv {input} results/qc/"

rule qc_report:
    input:
        rules.move_qc_output.output.eval_out
    output:
        "results/{sample}/{sample}.{word_length}mers.gkmqc.curve.pdf"
    params:
        gkmQC_path = config['paths']['gkmQC']
    shell:
        "python -E {params.gkmQC_path}/bin/gkmqc.py report -i {input} && "
        "cp results/qc/{wildcards.sample}.{wildcards.word_length}mers.gkmqc/{wildcards.sample}.{wildcards.word_length}mers.gkmqc.curve.pdf "
        "results/{wildcards.sample}"