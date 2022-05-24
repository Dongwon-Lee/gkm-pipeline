
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/gpfs/home/jtl334/.conda/envs/pipeline/lib/python3.7/site-packages', '/gpfs/scratch/jtl334/thesis/pipeline/workflow/scripts']); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05XH\x00\x00\x00data/tf_database/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.txtq\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x12\x00\x00\x00_allowed_overridesq\n]q\x0b(X\x05\x00\x00\x00indexq\x0cX\x04\x00\x00\x00sortq\reh\x0ccfunctools\npartial\nq\x0ecbuiltins\ngetattr\nq\x0fcsnakemake.io\nNamedlist\nq\x10X\x0f\x00\x00\x00_used_attributeq\x11\x86q\x12Rq\x13\x85q\x14Rq\x15(h\x13)}q\x16X\x05\x00\x00\x00_nameq\x17h\x0csNtq\x18bh\rh\x0eh\x13\x85q\x19Rq\x1a(h\x13)}q\x1bh\x17h\rsNtq\x1cbubX\x06\x00\x00\x00outputq\x1dcsnakemake.io\nOutputFiles\nq\x1e)\x81q\x1f(X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.0.txtq X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.1.txtq!X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.2.txtq"X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.3.txtq#X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.4.txtq$X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.5.txtq%X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.6.txtq&X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.7.txtq\'X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.8.txtq(X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.9.txtq)X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.10.txtq*X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.11.txtq+X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.12.txtq,X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.13.txtq-X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.14.txtq.X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.15.txtq/X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.16.txtq0X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.17.txtq1X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.18.txtq2X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.19.txtq3e}q4(h\x08}q5h\n]q6(h\x0ch\reh\x0ch\x0eh\x13\x85q7Rq8(h\x13)}q9h\x17h\x0csNtq:bh\rh\x0eh\x13\x85q;Rq<(h\x13)}q=h\x17h\rsNtq>bubX\x06\x00\x00\x00paramsq?csnakemake.io\nParams\nq@)\x81qAX8\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeqBa}qC(h\x08}qDX\t\x00\x00\x00target_fnqEK\x00N\x86qFsh\n]qG(h\x0ch\reh\x0ch\x0eh\x13\x85qHRqI(h\x13)}qJh\x17h\x0csNtqKbh\rh\x0eh\x13\x85qLRqM(h\x13)}qNh\x17h\rsNtqObhEhBubX\t\x00\x00\x00wildcardsqPcsnakemake.io\nWildcards\nqQ)\x81qRX3\x00\x00\x00JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeqSa}qT(h\x08}qUX\x10\x00\x00\x00tf_database_fileqVK\x00N\x86qWsh\n]qX(h\x0ch\reh\x0ch\x0eh\x13\x85qYRqZ(h\x13)}q[h\x17h\x0csNtq\\bh\rh\x0eh\x13\x85q]Rq^(h\x13)}q_h\x17h\rsNtq`bhVhSubX\x07\x00\x00\x00threadsqaK\x01X\t\x00\x00\x00resourcesqbcsnakemake.io\nResources\nqc)\x81qd(K\x01K\x01M\xe8\x03M\xe8\x03X\x04\x00\x00\x00/tmpqee}qf(h\x08}qg(X\x06\x00\x00\x00_coresqhK\x00N\x86qiX\x06\x00\x00\x00_nodesqjK\x01N\x86qkX\x06\x00\x00\x00mem_mbqlK\x02N\x86qmX\x07\x00\x00\x00disk_mbqnK\x03N\x86qoX\x06\x00\x00\x00tmpdirqpK\x04N\x86qquh\n]qr(h\x0ch\reh\x0ch\x0eh\x13\x85qsRqt(h\x13)}quh\x17h\x0csNtqvbh\rh\x0eh\x13\x85qwRqx(h\x13)}qyh\x17h\rsNtqzbhhK\x01hjK\x01hlM\xe8\x03hnM\xe8\x03hpheubX\x03\x00\x00\x00logq{csnakemake.io\nLog\nq|)\x81q}}q~(h\x08}q\x7fh\n]q\x80(h\x0ch\reh\x0ch\x0eh\x13\x85q\x81Rq\x82(h\x13)}q\x83h\x17h\x0csNtq\x84bh\rh\x0eh\x13\x85q\x85Rq\x86(h\x13)}q\x87h\x17h\rsNtq\x88bubX\x06\x00\x00\x00configq\x89}q\x8a(X\x06\x00\x00\x00sampleq\x8bX&\x00\x00\x00wgEncodeSydhTfbsGm12878Nfe2hStdAlnRep0q\x8cX\x0b\x00\x00\x00word_lengthq\x8dK\tX\x0f\x00\x00\x00min_word_lengthq\x8eK\x07X\x10\x00\x00\x00tf_metadata_fileq\x8fX\r\x00\x00\x00../TF_fam.txtq\x90X\x10\x00\x00\x00tf_database_fileq\x91X3\x00\x00\x00JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeq\x92uX\x04\x00\x00\x00ruleq\x93X\x0c\x00\x00\x00split_motifsq\x94X\x0f\x00\x00\x00bench_iterationq\x95NX\t\x00\x00\x00scriptdirq\x96X5\x00\x00\x00/gpfs/scratch/jtl334/thesis/pipeline/workflow/scriptsq\x97ub.'); from snakemake.logging import logger; logger.printshellcmds = False; __real_file__ = __file__; __file__ = '/gpfs/scratch/jtl334/thesis/pipeline/workflow/scripts/split_file.py';
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