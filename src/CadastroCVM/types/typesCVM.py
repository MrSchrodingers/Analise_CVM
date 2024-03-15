import pandas as pd

na_values = {
            'TP_FUNDO': 'NI',
            'CNPJ_FUNDO': 'NI',
            'DENOM_SOCIAL': 'NI',
            'CD_CVM': pd.NA,
            'SIT': 'NI',
            'DT_INI_SIT': pd.NaT,
            'DT_INI_ATIV': pd.NaT,
            'DT_INI_EXERC': pd.NaT,
            'DT_FIM_EXERC': pd.NaT,
            'CLASSE': 'NI',
            'DT_INI_CLASSE': pd.NaT,
            'RENTAB_FUNDO': 'NI',
            'CONDOM': 'NI',
            'FUNDO_COTAS': 'NI',
            'FUNDO_EXCLUSIVO': 'NI',
            'TRIB_LPRAZO': 'NI',
            'PUBLICO_ALVO': 'NI',
            'ENTID_INVEST': 'NI',
            'TAXA_PERFM': pd.NA,
            'INF_TAXA_PERFM': 'NI',
            'TAXA_ADM': pd.NA,
            'INF_TAXA_ADM': 'NI',
            'VL_PATRIM_LIQ': pd.NA,
            'DT_PATRIM_LIQ': pd.NaT,
            'DIRETOR': 'NI',
            'CNPJ_ADMIN': 'NI',
            'ADMIN': 'NI',
            'PF_PJ_GESTOR': 'NI',
            'CPF_CNPJ_GESTOR': 'NI',
            'GESTOR': 'NI',
            'CNPJ_AUDITOR': 'NI',
            'AUDITOR': 'NI',
            'CNPJ_CUSTODIANTE': 'NI',
            'CUSTODIANTE': 'NI',
            'CNPJ_CONTROLADOR': 'NI',
            'CONTROLADOR': 'NI',
            'INVEST_CEMPR_EXTER': 'NI',
            'CLASSE_ANBIMA': 'NI'
        }
dtype_dict = {
            'TP_FUNDO': str,
            'CNPJ_FUNDO': str,
            'DENOM_SOCIAL': str,
            'CD_CVM': float,
            'SIT': str,
            'CLASSE': str,
            'RENTAB_FUNDO': str,
            'CONDOM': str,
            'FUNDO_COTAS': str,
            'FUNDO_EXCLUSIVO': str,
            'TRIB_LPRAZO': str,
            'PUBLICO_ALVO': str,
            'ENTID_INVEST': str,
            'TAXA_PERFM': float,
            'INF_TAXA_PERFM': str,
            'TAXA_ADM': float,
            'INF_TAXA_ADM': str,
            'VL_PATRIM_LIQ': float,
            'DIRETOR': str,
            'CNPJ_ADMIN': str,
            'ADMIN': str,
            'PF_PJ_GESTOR': str,
            'CPF_CNPJ_GESTOR': str,
            'GESTOR': str,
            'CNPJ_AUDITOR': str,
            'AUDITOR': str,
            'CNPJ_CUSTODIANTE': str,
            'CUSTODIANTE': str,
            'CNPJ_CONTROLADOR': str,
            'CONTROLADOR': str,
            'INVEST_CEMPR_EXTER': str,
            'CLASSE_ANBIMA': str
        }

 