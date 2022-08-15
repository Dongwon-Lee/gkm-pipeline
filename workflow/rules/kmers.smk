# Runs scripts/nkmers.py to create fasta file containing all k-mers of word_length length
rule get_kmers:
    default_target: True
    output: 
        protected("data/kmers/{word_length}mers.fa")
    script:
        "scripts/nrkmers.py"