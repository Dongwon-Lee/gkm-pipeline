
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/gpfs/home/jtl334/.conda/envs/pipeline/lib/python3.7/site-packages', '/gpfs/scratch/jtl334/thesis/pipeline/workflow/scripts']); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05XH\x00\x00\x00data/tf_database/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.txtq\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x12\x00\x00\x00_allowed_overridesq\n]q\x0b(X\x05\x00\x00\x00indexq\x0cX\x04\x00\x00\x00sortq\reh\x0ccfunctools\npartial\nq\x0ecbuiltins\ngetattr\nq\x0fcsnakemake.io\nNamedlist\nq\x10X\x0f\x00\x00\x00_used_attributeq\x11\x86q\x12Rq\x13\x85q\x14Rq\x15(h\x13)}q\x16X\x05\x00\x00\x00_nameq\x17h\x0csNtq\x18bh\rh\x0eh\x13\x85q\x19Rq\x1a(h\x13)}q\x1bh\x17h\rsNtq\x1cbubX\x06\x00\x00\x00outputq\x1dcsnakemake.io\nOutputFiles\nq\x1e)\x81q\x1f(X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.0.txtq X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.1.txtq!X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.2.txtq"X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.3.txtq#X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.4.txtq$X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.5.txtq%X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.6.txtq&X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.7.txtq\'X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.8.txtq(X>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.9.txtq)X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.10.txtq*X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.11.txtq+X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.12.txtq,X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.13.txtq-X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.14.txtq.X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.15.txtq/X?\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.16.txtq0e}q1(h\x08}q2h\n]q3(h\x0ch\reh\x0ch\x0eh\x13\x85q4Rq5(h\x13)}q6h\x17h\x0csNtq7bh\rh\x0eh\x13\x85q8Rq9(h\x13)}q:h\x17h\rsNtq;bubX\x06\x00\x00\x00paramsq<csnakemake.io\nParams\nq=)\x81q>X8\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeq?a}q@(h\x08}qAX\t\x00\x00\x00target_fnqBK\x00N\x86qCsh\n]qD(h\x0ch\reh\x0ch\x0eh\x13\x85qERqF(h\x13)}qGh\x17h\x0csNtqHbh\rh\x0eh\x13\x85qIRqJ(h\x13)}qKh\x17h\rsNtqLbhBh?ubX\t\x00\x00\x00wildcardsqMcsnakemake.io\nWildcards\nqN)\x81qOX3\x00\x00\x00JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeqPa}qQ(h\x08}qRX\x10\x00\x00\x00tf_database_fileqSK\x00N\x86qTsh\n]qU(h\x0ch\reh\x0ch\x0eh\x13\x85qVRqW(h\x13)}qXh\x17h\x0csNtqYbh\rh\x0eh\x13\x85qZRq[(h\x13)}q\\h\x17h\rsNtq]bhShPubX\x07\x00\x00\x00threadsq^K\x01X\t\x00\x00\x00resourcesq_csnakemake.io\nResources\nq`)\x81qa(K\x01K\x01M\xe8\x03M\xe8\x03X\x04\x00\x00\x00/tmpqbe}qc(h\x08}qd(X\x06\x00\x00\x00_coresqeK\x00N\x86qfX\x06\x00\x00\x00_nodesqgK\x01N\x86qhX\x06\x00\x00\x00mem_mbqiK\x02N\x86qjX\x07\x00\x00\x00disk_mbqkK\x03N\x86qlX\x06\x00\x00\x00tmpdirqmK\x04N\x86qnuh\n]qo(h\x0ch\reh\x0ch\x0eh\x13\x85qpRqq(h\x13)}qrh\x17h\x0csNtqsbh\rh\x0eh\x13\x85qtRqu(h\x13)}qvh\x17h\rsNtqwbheK\x01hgK\x01hiM\xe8\x03hkM\xe8\x03hmhbubX\x03\x00\x00\x00logqxcsnakemake.io\nLog\nqy)\x81qz}q{(h\x08}q|h\n]q}(h\x0ch\reh\x0ch\x0eh\x13\x85q~Rq\x7f(h\x13)}q\x80h\x17h\x0csNtq\x81bh\rh\x0eh\x13\x85q\x82Rq\x83(h\x13)}q\x84h\x17h\rsNtq\x85bubX\x06\x00\x00\x00configq\x86}q\x87(X\x06\x00\x00\x00sampleq\x88X&\x00\x00\x00wgEncodeSydhTfbsGm12878Nfe2hStdAlnRep0q\x89X\x0b\x00\x00\x00word_lengthq\x8aK\tX\x0f\x00\x00\x00min_word_lengthq\x8bK\x07X\x10\x00\x00\x00tf_metadata_fileq\x8cX\r\x00\x00\x00../TF_fam.txtq\x8dX\x10\x00\x00\x00tf_database_fileq\x8eX3\x00\x00\x00JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeq\x8fuX\x04\x00\x00\x00ruleq\x90X\x0c\x00\x00\x00split_motifsq\x91X\x0f\x00\x00\x00bench_iterationq\x92NX\t\x00\x00\x00scriptdirq\x93X5\x00\x00\x00/gpfs/scratch/jtl334/thesis/pipeline/workflow/scriptsq\x94ub.'); from snakemake.logging import logger; logger.printshellcmds = False; __real_file__ = __file__; __file__ = '/gpfs/scratch/jtl334/thesis/pipeline/workflow/scripts/split_file.py';
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