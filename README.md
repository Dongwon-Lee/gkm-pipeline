# gkm-pipeline
A pipeline for discovery of likely CRE transcription factor elements from epigenomic sequencing data using the [LS-GKM](https://github.com/Dongwon-Lee/lsgkm) algorithm and built with [Snakemake](https://snakemake.readthedocs.io/en/stable/index.html).

### Setup
Gkm-pipeline requires functional installments of the [LS-GKM](https://github.com/Dongwon-Lee/lsgkm) and [gkmQC](https://github.com/Dongwon-Lee/gkmQC) to be present on the same machine. Please first follow the setup directions for both of those tools in order to use gkm-pipeline. (Note: you can skip the conda setup steps there, as gkm-pipeline requires its own conda environment).

To set up the [Conda](https://docs.conda.io/en/latest/) environment for gkm-pipeline, run the following in the project root directory:
```bash
$ conda env create -f environment.yml
$ conda activate gkm-pipeline
```

### Running the pipeline
In its most simple form, the pipeline can be run with the following command:
```bash
$ snakemake -c[cores]
```
This will run the entire pipeline, utilizing the number of Snakemake [cores](https://snakemake.readthedocs.io/en/stable/tutorial/advanced.html?highlight=cores#step-1-specifying-the-number-of-used-threads) specified to do so. However, before actually running an operation, it us reccommended to first perform a [dry run](https://snakemake.readthedocs.io/en/stable/tutorial/basics.html?highlight=dry-run#step-1-mapping-reads) of the operation like so:
```bash
$ snakemake -np
```
Where the `-n` command signals a dry run. A dry run shows what operations _would_ be performed if the command was run normally, without actually running them. The `-p` command prints the actual shell commands that would be run (which can be useful to check).

To run a specifc rule (and all prior rules whose output is required to run that rule), you can specify it like so
```bash
# Dry run
$ snakemake -np [rule name]
# Real run
$ snakemake -c[cores] [rule name]
```

Some of the pipeline steps can be given a variable amount of memory to speed up performance. You can specify a maximum amount of memory available to Snakemake (in MB) like so:
```bash
$ snakemake -c[cores] --resources mem_mb=[memory_in_MB]
```
The pipeline will automatically assign each step the maximum amount of memory specified by both the rule an the maximum given by the user.

### Pipeline steps
The pipeline consists of three main Snakemake [workflow modules](https://snakemake.readthedocs.io/en/stable/snakefiles/modularization.html#modules) which may be run separately by running an individual module's [target rule](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#targets-and-aggregation) or altogether by running the main target rule. They can be run as follows:

- `motif_database_all`: Runs only the steps needed to create the transcription factor sequence motif data file for the given transcription factor database. Outputs a file to the `data/tf_database` directory named `[tf_database_file].[word_length]_[min_word_length]mers.fimo.txt.gz`. Note that output of this rule is required to run the main `all` rule, however this is a long running process, so there may be situations in which one wants to run this rule separately. There are also precompiled TF sequence motif data files in the `data/tf_database` directory, which may be used to automatically skip this step when running the `all` rule.
- `qc_all`: Runs the gkmQC tool for the sample data. Outputs a `results/[sample]/[sample].[word_length]mers.gkmqc.curve.pdf` PDF file with a curve visualizing AUCs of trained QC models and the final gkmQC score
- `motif_enrichment_all`: Trains the LS-GKM model and motif enrichment pipeline which outputs the analysis of what TF motifs are enriched in the input file. Requires that the `motif_database` branch be ran first, and will run it if its output does not exist for the `word_length` and `min_word_length` values in the `config.yaml`. Outputs the following files to the `results/[sample]` directory:
  - `[sample].[word_length]mers.expr_enriched_tfs.html`: An HTML file containing information about all transcription factors found to be significantly upregulated for the sample data
  - `[sample].[word_length]mers.all_tfs.txt`: Text file continaing information about all transcription factors (including ones not found to be significant) 
  - `[sample].[word_length]mers.TF_class_enrichment_test.txt`: (Optional) Contains information about which TF classes are upregulated for the sample data
  - `[sample].[word_length]mers.TF_family_enrichment_test.txt`: (Optional) Contains information about which TF families are upregulated for the sample data
- `all` (or no rule specified): Runs all steps in the pipeline for which output doesn't already exist from start to finish

Note that any intermediate rule can also be given as a run argument to the pipeline.

### Configuration
Configuration of the pipeline and inputs/outputs is done by changing values in the `config/config.yaml` file. The available configuration variables are as follows:
- `samples`: An array of names of samples to be interrogated. The pipeline expects all samples to correspond with `.bed` files in the `data/samples` directory, i.e. `data/samples/[sample].bed`. Default: `example` (which points to an example sample file)
- `bed_score_col`: The column number containing the score rank in the input `.bed` file which the gkmQC tool will use to calculate the gkmQC score. Generally one of column number 7-9 (see https://genome.ucsc.edu/FAQ/FAQformat.html#format12). Default: 7
- `word_length`: The k-mer word length to use to train the LS-GKM algorithm. Default: 10
- `min_word_length`: When compiling the TF sequence motif data file, motif sequences in the database longer than `word_length` will need to be examined as smaller subsequences. `min_word_length` defines a value (_less than_ `word_length`) which is the minimum word length to consider for this process. Reccomended value: `word_length` - 2
- `tf_database_file`: Name of the motif database file present in `data/tf_database` as `[tf_database_file].txt`. This file should be in [MEME format](https://meme-suite.org/meme/doc/meme-format.html?man_type=web). Default: `JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme` (pre-provided JASPAR 2022 database of all vertebrate transcription factors, without redundancy) 
- `tf_metadata_file`: (Optional) Name of the file containing transcription factor family and class information. Should be a 3 column tsv file without headers in the format `Motif_ID TF_family TF_class`. Default: `TF_metadata` (pre-provided file of families and classes for motifs found in `JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.txt`)
- `enrichment_cutoffs`: Statistical cutoff values for determining whether a transcription factor is found to be significantly enriched for this sample. A TF is only considered significant if it passes _all three_ of the `enrichment_score`, `padj_cutoff_poisson`, and `padj_cutoff_wilcox` tests. Contains three values:
  - `percentile_cutoff`: Decimal value between 0-1 representing a percentile above which SVM weight cutoff a kmer is considered significant. Default: 0.05 (5th percentile)
  - `enrichment_score`: The number of kmers for the motif above the `percentile_cutoff`th percentile, divided by the total number of kmers for this motif, all divided by the `percentile_cutoff` value. I.e. (Kmer[`percentile_cutoff`*100]p / Total) / `percentile_cutoff`. Default: 2
  - `padj_cutoff_poisson`: Adjusted p-value cutoff for the Poisson test, which uses a Poisson distribution to determine whether the number of k-mers at the top `percentile_cutoff`th percentile of SVM weight is significantly higher than average. Default: `0.01`
  - `padj_cutoff_wilcox`: Adjusted p-value cutoff for the Wilcox test, which uses a Wilcoxon rank-sum test to determine whether the average SVM weight of the k-mers associated with a TF is significantly higher than the overall average SVM weight. Default: `0.01`
- `paths`:
  - `lsgkm`: Absolute path of [LS-GKM](https://github.com/Dongwon-Lee/lsgkm) program on this machine
  - `gkmQC`: Absolute path of [gkmQC](https://github.com/Dongwon-Lee/gkmQC) program on this machine

### Running the pipeline on a compute cluster
When running the pipeline on a clustering engine such as Slurm, take care to give at least as many resources to the cluster job as to Snakemake. For example:
```bash
#!/bin/bash

#SBATCH --job-name=gkm_pipeline
#SBATCH --time=12:00:00
#SBATCH --cpus-per-task=16
#SBATCH --mem=64GB

...

snakemake -c16 --resources mem_mb=63000
```
Note that the `cpus-per-task` are equal to or greater than the value of the cores argument passed to Snakemake, and `mem` is equal to or greater than the `mem_mb` argument passed to Snakemake.
