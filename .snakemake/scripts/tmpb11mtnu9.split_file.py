
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/gpfs/home/jtl334/.conda/envs/pipeline/lib/python3.7/site-packages', '/gpfs/scratch/jtl334/thesis/pipeline/workflow/scripts']); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05XH\x00\x00\x00data/tf_database/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.txtq\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x12\x00\x00\x00_allowed_overridesq\n]q\x0b(X\x05\x00\x00\x00indexq\x0cX\x04\x00\x00\x00sortq\reh\x0ccfunctools\npartial\nq\x0ecbuiltins\ngetattr\nq\x0fcsnakemake.io\nNamedlist\nq\x10X\x0f\x00\x00\x00_used_attributeq\x11\x86q\x12Rq\x13\x85q\x14Rq\x15(h\x13)}q\x16X\x05\x00\x00\x00_nameq\x17h\x0csNtq\x18bh\rh\x0eh\x13\x85q\x19Rq\x1a(h\x13)}q\x1bh\x17h\rsNtq\x1cbubX\x06\x00\x00\x00outputq\x1dcsnakemake.io\nOutputFiles\nq\x1e)\x81q\x1fX>\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.0.txtq a}q!(h\x08}q"h\n]q#(h\x0ch\reh\x0ch\x0eh\x13\x85q$Rq%(h\x13)}q&h\x17h\x0csNtq\'bh\rh\x0eh\x13\x85q(Rq)(h\x13)}q*h\x17h\rsNtq+bubX\x06\x00\x00\x00paramsq,csnakemake.io\nParams\nq-)\x81q.X8\x00\x00\x00temp/JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeq/a}q0(h\x08}q1X\t\x00\x00\x00target_fnq2K\x00N\x86q3sh\n]q4(h\x0ch\reh\x0ch\x0eh\x13\x85q5Rq6(h\x13)}q7h\x17h\x0csNtq8bh\rh\x0eh\x13\x85q9Rq:(h\x13)}q;h\x17h\rsNtq<bh2h/ubX\t\x00\x00\x00wildcardsq=csnakemake.io\nWildcards\nq>)\x81q?X3\x00\x00\x00JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeq@a}qA(h\x08}qBX\x10\x00\x00\x00tf_database_fileqCK\x00N\x86qDsh\n]qE(h\x0ch\reh\x0ch\x0eh\x13\x85qFRqG(h\x13)}qHh\x17h\x0csNtqIbh\rh\x0eh\x13\x85qJRqK(h\x13)}qLh\x17h\rsNtqMbhCh@ubX\x07\x00\x00\x00threadsqNK\x01X\t\x00\x00\x00resourcesqOcsnakemake.io\nResources\nqP)\x81qQ(K\x01K\x01M\xe8\x03M\xe8\x03X\x04\x00\x00\x00/tmpqRe}qS(h\x08}qT(X\x06\x00\x00\x00_coresqUK\x00N\x86qVX\x06\x00\x00\x00_nodesqWK\x01N\x86qXX\x06\x00\x00\x00mem_mbqYK\x02N\x86qZX\x07\x00\x00\x00disk_mbq[K\x03N\x86q\\X\x06\x00\x00\x00tmpdirq]K\x04N\x86q^uh\n]q_(h\x0ch\reh\x0ch\x0eh\x13\x85q`Rqa(h\x13)}qbh\x17h\x0csNtqcbh\rh\x0eh\x13\x85qdRqe(h\x13)}qfh\x17h\rsNtqgbhUK\x01hWK\x01hYM\xe8\x03h[M\xe8\x03h]hRubX\x03\x00\x00\x00logqhcsnakemake.io\nLog\nqi)\x81qj}qk(h\x08}qlh\n]qm(h\x0ch\reh\x0ch\x0eh\x13\x85qnRqo(h\x13)}qph\x17h\x0csNtqqbh\rh\x0eh\x13\x85qrRqs(h\x13)}qth\x17h\rsNtqububX\x06\x00\x00\x00configqv}qw(X\x06\x00\x00\x00sampleqxX&\x00\x00\x00wgEncodeSydhTfbsGm12878Nfe2hStdAlnRep0qyX\x0b\x00\x00\x00word_lengthqzK\tX\x0f\x00\x00\x00min_word_lengthq{K\x07X\x10\x00\x00\x00tf_metadata_fileq|X\r\x00\x00\x00../TF_fam.txtq}X\x10\x00\x00\x00tf_database_fileq~X3\x00\x00\x00JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeq\x7fuX\x04\x00\x00\x00ruleq\x80X\x0c\x00\x00\x00split_motifsq\x81X\x0f\x00\x00\x00bench_iterationq\x82NX\t\x00\x00\x00scriptdirq\x83X5\x00\x00\x00/gpfs/scratch/jtl334/thesis/pipeline/workflow/scriptsq\x84ub.'); from snakemake.logging import logger; logger.printshellcmds = False; __real_file__ = __file__; __file__ = '/gpfs/scratch/jtl334/thesis/pipeline/workflow/scripts/split_file.py';
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