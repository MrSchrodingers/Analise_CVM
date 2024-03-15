import os
import sys

import tempfile
import zipfile

import requests

import pandas as pd

sys.path.append('./CadastroCVM/types')
import typesInfoDiario as typesDiario

class FundSearch:
    def __init__(self):
        pass

    @staticmethod
    def download_zip(url: str, save_dir: str) -> bool:
        try:
            response = requests.get(url)
            response.raise_for_status()

            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(response.content)
                tmp_file.close()

                with zipfile.ZipFile(tmp_file.name, 'r') as zip_ref:
                    zip_ref.extractall(save_dir)
            
            os.remove(tmp_file.name)
            
            return True
        except Exception as e:
            print(f"Error downloading the zip file: {e}")
            return False

    @staticmethod
    def filter_by_cnpj(csv_path: str, cnpj: str) -> pd.DataFrame:
        try:
            convert_date_columns = ['DT_COMPTC']
            
            df = pd.read_csv(csv_path, sep=';', na_values=typesDiario.na_values)
            df_filtered = df[df['CNPJ_FUNDO'] == cnpj]
            
            for col in convert_date_columns:
                    df[col] = pd.to_datetime(df[col], format='%Y-%m-%d')
                    
            return df_filtered
        except Exception as e:
            print(f"Error filtering by CNPJ: {e}")
            return pd.DataFrame()

    @staticmethod
    def extract_data_by_cnpj(cnpj: str, start_year: int, end_year: int) -> pd.DataFrame:
        total_data = pd.DataFrame()
        for year in range(start_year, end_year + 1):
            for month in range(1, 13):
                if year < 2021:
                    url = f'https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/HIST/inf_diario_fi_{year:02d}{month:02d}.zip'
                else:
                    url = f'https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{year:02d}{month:02d}.zip'

                temp_dir = tempfile.mkdtemp()
                zip_file_path = os.path.join(temp_dir, f'inf_diario_fi_{year:02d}{month:02d}.zip')

                if FundSearch.download_zip(url, temp_dir):
                    csv_file_path = os.path.join(temp_dir, f'inf_diario_fi_{year:02d}{month:02d}.csv')
                    df_month = FundSearch.filter_by_cnpj(csv_file_path, cnpj)
                    if not df_month.empty:
                        total_data = pd.concat([total_data, df_month], ignore_index=True)

        return total_data
