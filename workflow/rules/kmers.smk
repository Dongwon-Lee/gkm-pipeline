rule get_kmers:
    default_target: True
    output: 
        protected("data/kmers/{word_length}mers.fa")
    script:
        "scripts/nrkmers.py"