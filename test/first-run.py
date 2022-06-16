import pandas as pd


def get_template_columns(ref_gwas, target_gwas, right_on, left_on):

    ref_gwas = ref_gwas.copy()
    target_gwas = target_gwas.copy()

    ref_gwas.columns = ref_gwas.columns.str.replace('_harmonized', '')
    target_gwas.columns = target_gwas.columns.str.replace('_harmonized', '')
    right_on = right_on.replace('_harmonized', '')
    left_on = left_on.replace('_harmonized', '')

    merged = ref_gwas.merge(target_gwas, right_on=right_on,
                            left_on=left_on, how='right')

    original_SNP_name = [el for el in target_gwas.columns if 'SNP' in el][0]
    merged_dedup = merged.drop_duplicates(
        subset=f'{original_SNP_name}_y', keep='first')

    merged_dedup['ALLELE1_x'] = merged_dedup['ALLELE1_x'].fillna('NAN')
    merged_dedup['ALLELE0_x'] = merged_dedup['ALLELE0_x'].fillna('NAN')
    res = perform_EA_homogenization(
        df=merged_dedup,
        col_ea_exposure='ALLELE1_x',
        col_nea_exposure='ALLELE0_x',
        col_eaf_exposure='A1FREQ_x',
        col_ea_outcome='ALLELE1_y',
        col_nea_outcome='ALLELE0_y',
        col_eaf_outcome='A1FREQ_y',
        col_beta_outcome='BETA_y'
    )

    try:
        template = res.loc[:, [right_on, 'SNP_y',
                               'ALLELE1_y', 'ALLELE0_y', 'A1FREQ_y', 'BETA_y']]
    except:
        template = res.loc[:, ['SNP_y', 'SNP_y',
                               'ALLELE1_y', 'ALLELE0_y', 'A1FREQ_y', 'BETA_y']]
    template.columns = ['rsid_harmonized'] + [el +
                                              '_harmonized' for el in template.columns.str.replace('_y', '')][1:]
    return template


def perform_EA_homogenization(df, col_beta_outcome, col_eaf_outcome, col_nea_outcome, col_ea_outcome, col_eaf_exposure, col_nea_exposure, col_ea_exposure):
    return pd.DataFrame()
