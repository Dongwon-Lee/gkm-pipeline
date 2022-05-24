import sys
import pandas as pd
import numpy as np
import math 
from scipy.stats import poisson, mannwhitneyu, fisher_exact
import os

args = sys.argv
svmwf = args[1]
motif_db_fn = args[2]
outprefix = args[3]
kmer5p_pcrt_cutoff = float(args[4])
padj_cutoff_poisson = float(args[5])
padj_cutoff_wilcox = float(args[6])
tf_metadata_fn = args[7]

x = pd.read_csv(motif_db_fn, sep='\t', names=['TF_Name', 'Motif_ID', 'kmer'])
kmer_motif = x[['Motif_ID', 'kmer']]
TF_motif = x[['TF_Name', 'Motif_ID']].drop_duplicates()
kmersvmw = pd.read_csv(svmwf, sep='\t', names=['kmer', 'svmw'])
allKmerSample = kmersvmw if kmersvmw.shape[0] < 10000 else kmersvmw.sample(10000)

kmer_motif = kmer_motif.merge(kmersvmw, how='left', on='kmer')

sorted_svmw = kmersvmw.sort_values('svmw')
nkmers = sorted_svmw.shape[0]
svmw5p_cutoff = sorted_svmw.iloc[math.floor(nkmers*0.95)]['svmw']

xn = kmer_motif.groupby('Motif_ID').size().reset_index(name='total')
xn5 = kmer_motif[kmer_motif['svmw'] > svmw5p_cutoff].groupby('Motif_ID').size().reset_index(name='kmer5p')

motinfo = xn.merge(xn5, how='left', on='Motif_ID')
motinfo = motinfo.merge(TF_motif, how='left', on='Motif_ID')
motinfo= motinfo.fillna(0)

def computeRankSum(row):
    motif = row['Motif_ID']
    kmerForMotif = kmer_motif[kmer_motif['Motif_ID'] == motif]
    otherkmers = allKmerSample[~allKmerSample['kmer'].isin(kmerForMotif['kmer'])]
    pval =  mannwhitneyu(kmerForMotif['svmw'], otherkmers['svmw'], alternative='greater').pvalue 
    return pval

motinfo['kmer5p_pcrt'] = motinfo['kmer5p'] / motinfo['total']
motinfo['poisson_pval'] = motinfo.apply(lambda row: poisson.sf(row['kmer5p']-1, row['total']*0.05), axis=1)
motinfo['padj_poisson'] = motinfo['poisson_pval'] * motinfo.shape[0]
motinfo.loc[motinfo['padj_poisson'] > 1, 'padj_poisson'] = 1

motinfo['wilcox_pval'] = motinfo.apply(computeRankSum , axis=1)
motinfo['padj_wilcox'] = motinfo['wilcox_pval'] * motinfo.shape[0]
motinfo.loc[motinfo['padj_wilcox'] > 1, 'padj_wilcox'] = 1

motinfo.loc[motinfo['poisson_pval'] == 0, 'poisson_pval'] = sys.float_info.min
motinfo.loc[motinfo['padj_poisson'] == 0, 'padj_poisson'] = sys.float_info.min
motinfo.loc[motinfo['wilcox_pval'] == 0, 'wilcox_pval'] = sys.float_info.min
motinfo.loc[motinfo['padj_wilcox'] == 0, 'padj_wilcox'] = sys.float_info.min

motinfo['is_sig'] = (motinfo['padj_poisson'] <= padj_cutoff_poisson) & (motinfo['padj_wilcox'] <= padj_cutoff_wilcox) & (motinfo['kmer5p_pcrt'] >= kmer5p_pcrt_cutoff)

expr_enriched_tfs = motinfo.loc[motinfo['is_sig'], ['TF_Name', 'Motif_ID', 'total', 'kmer5p', 'kmer5p_pcrt', 'poisson_pval', 'padj_poisson', 'wilcox_pval', 'padj_wilcox']]
filename = f'{outprefix}.expr_enriched_tfs.txt'
expr_enriched_tfs.to_csv(filename, index=False, sep='\t', float_format='%.16g')

if tf_metadata_fn:
    tf_metadata = pd.read_csv(tf_metadata_fn, sep='\t',names=['Motif_ID', 'Family', 'Class'])
    motinfo = motinfo.merge(tf_metadata, how='left', on='Motif_ID')

    totalTfs = motinfo.shape[0]
    num_sig = motinfo[motinfo['is_sig']].shape[0]

    families = tf_metadata['Family'].dropna().unique()
    res_fam = pd.DataFrame(columns = ['Family', 'm00', 'm01', 'm10', 'm11', 'fisher_pval'])
    for family in families:
        num_in_fam = motinfo[motinfo['Family'] == family].shape[0]
        m11 = motinfo[(motinfo['Family'] == family) & motinfo['is_sig']].shape[0]
        m10 = num_in_fam - m11
        m01 = num_sig - m11
        m00 = totalTfs - (m11 + m10 + m01)
        oddsratio, pvalue = fisher_exact([[m00, m01], [m10, m11]], alternative='greater')
        res_fam = res_fam.append({'Family': family, 'm00': m00, 'm01': m01, 'm10': m10, 'm11': m11, 'fisher_pval': pvalue}, ignore_index=True)

    filename = f'{outprefix}.TF_family_enrichment_test.txt'
    res_fam.to_csv(filename, index=False, sep='\t', float_format='%.16g')

    classes = tf_metadata['Class'].dropna().unique()
    res_class = pd.DataFrame(columns = ['Class', 'm00', 'm01', 'm10', 'm11', 'fisher_pval'])
    for cls in classes:
        num_in_class = motinfo[motinfo['Class'] == cls].shape[0]
        m11 = motinfo[(motinfo['Class'] == cls) & motinfo['is_sig']].shape[0]
        m10 = num_in_class - m11
        m01 = num_sig - m11
        m00 = totalTfs - (m11 + m10 + m01)
        oddsratio, pvalue = fisher_exact([[m00, m01], [m10, m11]], alternative='greater')
        res_class = res_class.append({'Class': cls, 'm00': m00, 'm01': m01, 'm10': m10, 'm11': m11, 'fisher_pval': pvalue}, ignore_index=True)

    filename = f'{outprefix}.TF_class_enrichment_test.txt'
    res_class.to_csv(filename, index=False, sep='\t', float_format='%.16g')