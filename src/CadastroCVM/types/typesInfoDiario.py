import pandas as pd
import numpy as np


na_values = {
    'TP_FUNDO': pd.NA,
    'CNPJ_FUNDO': pd.NA,
    'DT_COMPTC': pd.NaT,
    'VL_TOTAL': pd.NA,
    'VL_QUOTA': pd.NA,
    'VL_PATRIM_LIQ': pd.NA,
    'CAPTC_DIA': pd.NA,
    'RESG_DIA': pd.NA,
    'NR_COTST': pd.NA,
}

dtype_dict = {
    'TP_FUNDO': str,
    'CNPJ_FUNDO': str,
    'DT_COMPTC' : 'object',
    'VL_TOTAL': np.float64,
    'VL_QUOTA': np.float64,
    'VL_PATRIM_LIQ': np.float64,
    'CAPTC_DIA': np.float64,
    'RESG_DIA': np.float64,
    'NR_COTST': np.float64,
}
