# Import kmers snakefile
module kmers:
    snakefile: 'kmers.smk'
    config: config

use rule * from kmers as kmers_* 

# Default target which runs all motif database creation steps 
rule all:
    default_target: True
    input:
        expand("data/tf_database/{tf_database_file}.{word_length}_{min_word_length}mers.fimo.txt.gz", tf_database_file=config['tf_database_file'], word_length=config["word_length"], min_word_length=config["min_word_length"])

# Runs scripts/split_file.py to split tf database file by number of available threads, 
# then run FIMO for each split file in its own thread
rule split_and_run_fimo:
    input:
        db_file = "data/tf_database/{tf_database_file}.txt",
        kmers = rules.kmers_get_kmers.output,
    output:
        temp(expand("tmp/{{tf_database_file}}.{{word_length}}_{{min_word_length}}mers.{i}.fimo.txt", i=range(workflow.cores)))
    threads: workflow.cores
    resources: 
        tmpdir = 'tmp/'
    script:
        "../scripts/split_file.py"

# Combines the output of each FIMO thread into one database file
rule combine_fimo_output:
    input: 
        rules.split_and_run_fimo.output
    output:
        protected("data/tf_database/{tf_database_file}.{word_length}_{min_word_length}mers.fimo.txt.gz")
    resources: 
        tmpdir = 'tmp/'
    params:
        tmp_file = '$TMPDIR/{tf_database_file}.{word_length}_{min_word_length}mers.fimo.txt'
    shell:
        """
        cat {input} | grep -v 'motif' > {params.tmp_file}
        cut -f 2 {params.tmp_file} | \
        cut -d '_' -f 1 | \
        paste - {params.tmp_file} | \
        cut -f 1,2,4 | \
        sort -u | gzip -c > {output}
        rm {params.tmp_file}
        """