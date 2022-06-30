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
percent = float(args[4])
enrichment_score_cutoff = float(args[5])
padj_cutoff_poisson = float(args[6])
padj_cutoff_wilcox = float(args[7])
tf_metadata_fn = args[8]

top_percentile = percent * 100
percentile_col = f'kmer{top_percentile}p'

x = pd.read_csv(motif_db_fn, sep='\t', names=['TF_Name', 'Motif_ID', 'kmer'])
kmer_motif = x[['Motif_ID', 'kmer']]
TF_motif = x[['TF_Name', 'Motif_ID']].drop_duplicates()
kmersvmw = pd.read_csv(svmwf, sep='\t', names=['kmer', 'svmw'])
allKmerSample = kmersvmw if kmersvmw.shape[0] < 10000 else kmersvmw.sample(10000)

kmer_motif = kmer_motif.merge(kmersvmw, how='left', on='kmer')

sorted_svmw = kmersvmw.sort_values('svmw')
nkmers = sorted_svmw.shape[0]
svmwp_cutoff = sorted_svmw.iloc[math.floor(nkmers*(1-percent))]['svmw']

xn = kmer_motif.groupby('Motif_ID').size().reset_index(name='total')
xn5 = kmer_motif[kmer_motif['svmw'] > svmwp_cutoff].groupby('Motif_ID').size().reset_index(name=percentile_col)

motinfo = xn.merge(xn5, how='left', on='Motif_ID')
motinfo = motinfo.merge(TF_motif, how='left', on='Motif_ID')
motinfo= motinfo.fillna(0)

def computeRankSum(row):
    motif = row['Motif_ID']
    kmerForMotif = kmer_motif[kmer_motif['Motif_ID'] == motif]
    otherkmers = allKmerSample[~allKmerSample['kmer'].isin(kmerForMotif['kmer'])]
    pval =  mannwhitneyu(kmerForMotif['svmw'], otherkmers['svmw'], alternative='greater').pvalue 
    return pval

motinfo['enrichment_score'] = (motinfo[percentile_col] / motinfo['total']) / percent
motinfo['poisson_pval'] = motinfo.apply(lambda row: poisson.sf(row[percentile_col]-1, row['total']*percent), axis=1)
motinfo['padj_poisson'] = motinfo['poisson_pval'] * motinfo.shape[0]
motinfo.loc[motinfo['padj_poisson'] > 1, 'padj_poisson'] = 1

motinfo['wilcox_pval'] = motinfo.apply(computeRankSum , axis=1)
motinfo['padj_wilcox'] = motinfo['wilcox_pval'] * motinfo.shape[0]
motinfo.loc[motinfo['padj_wilcox'] > 1, 'padj_wilcox'] = 1

motinfo.loc[motinfo['poisson_pval'] == 0, 'poisson_pval'] = sys.float_info.min
motinfo.loc[motinfo['padj_poisson'] == 0, 'padj_poisson'] = sys.float_info.min
motinfo.loc[motinfo['wilcox_pval'] == 0, 'wilcox_pval'] = sys.float_info.min
motinfo.loc[motinfo['padj_wilcox'] == 0, 'padj_wilcox'] = sys.float_info.min

motinfo['is_sig'] = (motinfo['padj_poisson'] <= padj_cutoff_poisson) & (motinfo['padj_wilcox'] <= padj_cutoff_wilcox) & (motinfo['enrichment_score'] >= enrichment_score_cutoff)

def makeHtmlFile(htmlString):
    return f'''<!DOCTYPE html>
<html>
    <head>
        <link href="https://tofsjonas.github.io/sortable/sortable.css" rel="stylesheet" />
        <script src="https://tofsjonas.github.io/sortable/sortable.js"></script>
        <style>
            th, td {{padding: 4px !important;}}
            img {{max-height: 80px;}}
            table {{font-size: 0.85em; text-align: center;}}
        </style>
    </head>
    <body>
        {htmlString}
    </body>
</html>
'''

if tf_metadata_fn:
    tf_metadata = pd.read_csv(tf_metadata_fn, sep='\t',names=['Motif_ID', 'Family', 'Class'])
    motinfo = motinfo.merge(tf_metadata, how='left', on='Motif_ID')

    filename = f'{outprefix}.all_tfs.txt'
    motinfo.to_csv(filename, sep='\t', index=False, float_format='%.8g')

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
    res_fam.to_csv(filename, index=False, sep='\t', float_format='%.8g')

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
    res_class.to_csv(filename, index=False, sep='\t', float_format='%.8g')

    expr_enriched_tfs = motinfo.loc[motinfo['is_sig'], ['TF_Name', 'Motif_ID', 'Family', 'Class', 'total', percentile_col, 'enrichment_score', 'poisson_pval', 'padj_poisson', 'wilcox_pval', 'padj_wilcox']]
    expr_enriched_tfs['Logo'] = expr_enriched_tfs['Motif_ID'].map('<img src="https://jaspar.genereg.net/static/logos/all/svg/{}.svg"/>'.format)
    expr_enriched_tfs['Motif_ID'] = expr_enriched_tfs['Motif_ID'].map(lambda x: f'<a target="_blank" href="http://jaspar.genereg.net/matrix/{x}">{x}</a>')
    file = open(f'{outprefix}.expr_enriched_tfs.html', 'w')
    file.write(makeHtmlFile(expr_enriched_tfs.to_html(index=False, classes='sortable', escape=False, float_format='%.8g')))
    file.close()
else:
    filename = f'{outprefix}.all_tfs.txt'
    motinfo.to_csv(filename, sep='\t', index=False, float_format='%.8g')
    expr_enriched_tfs = motinfo.loc[motinfo['is_sig'], ['TF_Name', 'Motif_ID', 'total', percentile_col, 'enrichment_score', 'poisson_pval', 'padj_poisson', 'wilcox_pval', 'padj_wilcox']]
    expr_enriched_tfs['Logo'] = expr_enriched_tfs['Motif_ID'].map('<img src="https://jaspar.genereg.net/static/logos/all/svg/{}.svg"/>'.format)
    expr_enriched_tfs['Motif_ID'] = expr_enriched_tfs['Motif_ID'].map(lambda x: f'<a target="_blank" href="http://jaspar.genereg.net/matrix/{x}">{x}</a>')
    file = open(f'{outprefix}.expr_enriched_tfs.html', 'w')
    file.write(makeHtmlFile(expr_enriched_tfs.to_html(index=False, classes='sortable', escape=False, float_format='%.8g')))
    file.close()