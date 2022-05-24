
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/gpfs/home/jtl334/.conda/envs/pipeline/lib/python3.7/site-packages', '/gpfs/scratch/jtl334/thesis/pipeline/workflow/scripts']); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05XH\x00\x00\x00data/tf_database/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.txtq\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x12\x00\x00\x00_allowed_overridesq\n]q\x0b(X\x05\x00\x00\x00indexq\x0cX\x04\x00\x00\x00sortq\reh\x0ccfunctools\npartial\nq\x0ecbuiltins\ngetattr\nq\x0fcsnakemake.io\nNamedlist\nq\x10X\x0f\x00\x00\x00_used_attributeq\x11\x86q\x12Rq\x13\x85q\x14Rq\x15(h\x13)}q\x16X\x05\x00\x00\x00_nameq\x17h\x0csNtq\x18bh\rh\x0eh\x13\x85q\x19Rq\x1a(h\x13)}q\x1bh\x17h\rsNtq\x1cbubX\x06\x00\x00\x00outputq\x1dcsnakemake.io\nOutputFiles\nq\x1e)\x81q\x1fXJ\x00\x00\x00data/tf_database/JASPAR2022_CORE_vertebrates_non-redundant_pfms_meme.0.txtq a}q!(h\x08}q"h\n]q#(h\x0ch\reh\x0ch\x0eh\x13\x85q$Rq%(h\x13)}q&h\x17h\x0csNtq\'bh\rh\x0eh\x13\x85q(Rq)(h\x13)}q*h\x17h\rsNtq+bubX\x06\x00\x00\x00paramsq,csnakemake.io\nParams\nq-)\x81q.K\x01a}q/(h\x08}q0X\t\x00\x00\x00num_filesq1K\x00N\x86q2sh\n]q3(h\x0ch\reh\x0ch\x0eh\x13\x85q4Rq5(h\x13)}q6h\x17h\x0csNtq7bh\rh\x0eh\x13\x85q8Rq9(h\x13)}q:h\x17h\rsNtq;bh1K\x01ubX\t\x00\x00\x00wildcardsq<csnakemake.io\nWildcards\nq=)\x81q>X3\x00\x00\x00JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeq?a}q@(h\x08}qAX\x10\x00\x00\x00tf_database_fileqBK\x00N\x86qCsh\n]qD(h\x0ch\reh\x0ch\x0eh\x13\x85qERqF(h\x13)}qGh\x17h\x0csNtqHbh\rh\x0eh\x13\x85qIRqJ(h\x13)}qKh\x17h\rsNtqLbhBh?ubX\x07\x00\x00\x00threadsqMK\x01X\t\x00\x00\x00resourcesqNcsnakemake.io\nResources\nqO)\x81qP(K\x01K\x01M\xe8\x03M\xe8\x03X\x04\x00\x00\x00/tmpqQe}qR(h\x08}qS(X\x06\x00\x00\x00_coresqTK\x00N\x86qUX\x06\x00\x00\x00_nodesqVK\x01N\x86qWX\x06\x00\x00\x00mem_mbqXK\x02N\x86qYX\x07\x00\x00\x00disk_mbqZK\x03N\x86q[X\x06\x00\x00\x00tmpdirq\\K\x04N\x86q]uh\n]q^(h\x0ch\reh\x0ch\x0eh\x13\x85q_Rq`(h\x13)}qah\x17h\x0csNtqbbh\rh\x0eh\x13\x85qcRqd(h\x13)}qeh\x17h\rsNtqfbhTK\x01hVK\x01hXM\xe8\x03hZM\xe8\x03h\\hQubX\x03\x00\x00\x00logqgcsnakemake.io\nLog\nqh)\x81qi}qj(h\x08}qkh\n]ql(h\x0ch\reh\x0ch\x0eh\x13\x85qmRqn(h\x13)}qoh\x17h\x0csNtqpbh\rh\x0eh\x13\x85qqRqr(h\x13)}qsh\x17h\rsNtqtbubX\x06\x00\x00\x00configqu}qv(X\x06\x00\x00\x00sampleqwX&\x00\x00\x00wgEncodeSydhTfbsGm12878Nfe2hStdAlnRep0qxX\x0b\x00\x00\x00word_lengthqyK\tX\x0f\x00\x00\x00min_word_lengthqzK\x07X\x10\x00\x00\x00tf_metadata_fileq{X\r\x00\x00\x00../TF_fam.txtq|X\x10\x00\x00\x00tf_database_fileq}X3\x00\x00\x00JASPAR2022_CORE_vertebrates_non-redundant_pfms_memeq~uX\x04\x00\x00\x00ruleq\x7fX\x0c\x00\x00\x00split_motifsq\x80X\x0f\x00\x00\x00bench_iterationq\x81NX\t\x00\x00\x00scriptdirq\x82X5\x00\x00\x00/gpfs/scratch/jtl334/thesis/pipeline/workflow/scriptsq\x83ub.'); from snakemake.logging import logger; logger.printshellcmds = False; __real_file__ = __file__; __file__ = '/gpfs/scratch/jtl334/thesis/pipeline/workflow/scripts/split_file.py';
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

dbFile = snakemake.input['db_file']
numFiles = snakemake.input['num_files']
k_min = snakemake.config['min_word_length']
k = snakemake.config['word_length']    
subMers = k - k_min

print(f'there are {numFiles} threads avail')

files = []
for i in range(numFiles):
    file = open(f'{os.path.splitext(dbFile)[0]}.{i}.txt', 'w')
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