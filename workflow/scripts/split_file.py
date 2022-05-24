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