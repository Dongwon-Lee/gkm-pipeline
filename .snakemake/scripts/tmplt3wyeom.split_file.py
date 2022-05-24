
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/gpfs/home/jtl334/.conda/envs/pipeline/lib/python3.7/site-packages', '/gpfs/scratch/jtl334/thesis/pipeline/workflow/scripts']); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05XH\x00\x00\x00data/tf_database/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.txtq\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x12\x00\x00\x00_allowed_overridesq\n]q\x0b(X\x05\x00\x00\x00indexq\x0cX\x04\x00\x00\x00sortq\reh\x0ccfunctools\npartial\nq\x0ecbuiltins\ngetattr\nq\x0fcsnakemake.io\nNamedlist\nq\x10X\x0f\x00\x00\x00_used_attributeq\x11\x86q\x12Rq\x13\x85q\x14Rq\x15(h\x13)}q\x16X\x05\x00\x00\x00_nameq\x17h\x0csNtq\x18bh\rh\x0eh\x13\x85q\x19Rq\x1a(h\x13)}q\x1bh\x17h\rsNtq\x1cbubX\x06\x00\x00\x00outputq\x1dcsnakemake.io\nOutputFiles\nq\x1e)\x81q\x1f(X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.0.txtq X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.1.txtq!X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.2.txtq"X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.3.txtq#X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.4.txtq$X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.5.txtq%X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.6.txtq&X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.7.txtq\'X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.8.txtq(X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.9.txtq)e}q*(h\x08}q+h\n]q,(h\x0ch\reh\x0ch\x0eh\x13\x85q-Rq.(h\x13)}q/h\x17h\x0csNtq0bh\rh\x0eh\x13\x85q1Rq2(h\x13)}q3h\x17h\rsNtq4bubX\x06\x00\x00\x00paramsq5csnakemake.io\nParams\nq6)\x81q7X8\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeq8a}q9(h\x08}q:X\t\x00\x00\x00target_fnq;K\x00N\x86q<sh\n]q=(h\x0ch\reh\x0ch\x0eh\x13\x85q>Rq?(h\x13)}q@h\x17h\x0csNtqAbh\rh\x0eh\x13\x85qBRqC(h\x13)}qDh\x17h\rsNtqEbh;h8ubX\t\x00\x00\x00wildcardsqFcsnakemake.io\nWildcards\nqG)\x81qHX3\x00\x00\x00JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeqIa}qJ(h\x08}qKX\x10\x00\x00\x00tf_database_fileqLK\x00N\x86qMsh\n]qN(h\x0ch\reh\x0ch\x0eh\x13\x85qORqP(h\x13)}qQh\x17h\x0csNtqRbh\rh\x0eh\x13\x85qSRqT(h\x13)}qUh\x17h\rsNtqVbhLhIubX\x07\x00\x00\x00threadsqWK\x01X\t\x00\x00\x00resourcesqXcsnakemake.io\nResources\nqY)\x81qZ(K\x01K\x01M\xe8\x03M\xe8\x03X\x04\x00\x00\x00/tmpq[e}q\\(h\x08}q](X\x06\x00\x00\x00_coresq^K\x00N\x86q_X\x06\x00\x00\x00_nodesq`K\x01N\x86qaX\x06\x00\x00\x00mem_mbqbK\x02N\x86qcX\x07\x00\x00\x00disk_mbqdK\x03N\x86qeX\x06\x00\x00\x00tmpdirqfK\x04N\x86qguh\n]qh(h\x0ch\reh\x0ch\x0eh\x13\x85qiRqj(h\x13)}qkh\x17h\x0csNtqlbh\rh\x0eh\x13\x85qmRqn(h\x13)}qoh\x17h\rsNtqpbh^K\x01h`K\x01hbM\xe8\x03hdM\xe8\x03hfh[ubX\x03\x00\x00\x00logqqcsnakemake.io\nLog\nqr)\x81qs}qt(h\x08}quh\n]qv(h\x0ch\reh\x0ch\x0eh\x13\x85qwRqx(h\x13)}qyh\x17h\x0csNtqzbh\rh\x0eh\x13\x85q{Rq|(h\x13)}q}h\x17h\rsNtq~bubX\x06\x00\x00\x00configq\x7f}q\x80(X\x06\x00\x00\x00sampleq\x81X&\x00\x00\x00wgEncodeSydhTfbsGm12878Nfe2hStdAlnRep0q\x82X\x0b\x00\x00\x00word_lengthq\x83K\tX\x0f\x00\x00\x00min_word_lengthq\x84K\x07X\x10\x00\x00\x00tf_metadata_fileq\x85X\r\x00\x00\x00../TF_fam.txtq\x86X\x10\x00\x00\x00tf_database_fileq\x87X3\x00\x00\x00JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeq\x88uX\x04\x00\x00\x00ruleq\x89X\x0c\x00\x00\x00split_motifsq\x8aX\x0f\x00\x00\x00bench_iterationq\x8bNX\t\x00\x00\x00scriptdirq\x8cX5\x00\x00\x00/gpfs/scratch/jtl334/thesis/pipeline/workflow/scriptsq\x8dub.'); from snakemake.logging import logger; logger.printshellcmds = False; __real_file__ = __file__; __file__ = '/gpfs/scratch/jtl334/thesis/pipeline/workflow/scripts/split_file.py';
######## snakemake preamble end #########
#!/usr/bin/env python3

import re
import os

memeHeader = '''MEME version 4

ALPHABET= ACGT

strands: + -

Background letter frequencies
A 0.25 C 0.25 G 0.25 T 0.25

'''

dbFile = snakemake.input[0]
numFiles = len(snakemake.output)
k_min = snakemake.config['min_word_length']
k = snakemake.config['word_length']    
subMers = k - k_min

print(f'there are {numFiles} cores avail')

files = []
for i in range(numFiles):
    file = open(f'{snakemake.params["target_fn"]}.{i}.txt', 'w')
    if i > 0: file.write(memeHeader)
    files.append(file)

with open(dbFile, "r") as fp:
    i = 0
    motif = []
    for line in fp:
        if line.startswith('MOTIF'):
            files[i%numFiles].write('\n'.join(motif))
            i+=1
            motif = [line.strip()]
        elif line.startswith('URL'):
            motif.append(line)
            freqData = motif[2:-1]
            curK = len(freqData)
            if curK > k:
                motifName = motif[0].strip()
                headerValues = re.findall('\d+', motif[1])
                url = motif[-1]
                motif = []
                for startInd in range(curK - k_min + 1):
                    for endInd in range(k_min + startInd - 1, min(curK, startInd + k_min + subMers)):
                        subMotifName = f'{motifName}_{startInd}_{endInd}'
                        subMotif = freqData[startInd:endInd + 1]
                        motif.append(subMotifName)
                        motif.append(f'letter-probability matrix: alength= {headerValues[0]} w= {len(subMotif)} nsites= {headerValues[2]} E= {headerValues[3]}')
                        motif += subMotif
                        motif.append(url)
                    
        else:
            motif.append(line.strip())
                                
for i in range(numFiles):
    files[i].close()