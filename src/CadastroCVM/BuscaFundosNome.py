import os
import sys

import requests

import pandas as pd
from collections import defaultdict

from fuzzywuzzy import fuzz

sys.path.append('./CadastroCVM/types')
import typesCVM as typesCVM
current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, './CadastroCVM/types'))

class FundNameSearch:
    def __init__(self):
        pass

    @staticmethod
    def search_cvm_registration():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, '../../public/cadastroCVM/cad_fi.csv')

        try:
            target_dir = os.path.join(current_dir, '../../public/cadastroCVM/')
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                print('Directory "cadastroCVM" created in /public.')

            if os.path.exists(file_path):
                print('The FI registration file already exists. Loading data...')
                df = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1', na_values=typesCVM.na_values)
            else:
                url = "http://dados.cvm.gov.br/dados/FI/CAD/DADOS/cad_fi.csv"
                response = requests.get(url)
                response.raise_for_status()

                convert_date_columns = ['DT_INI_SIT', 'DT_INI_ATIV', 'DT_INI_EXERC', 'DT_FIM_EXERC', 'DT_INI_CLASSE', 'DT_PATRIM_LIQ']
                dtype_dict = typesCVM.dtype_dict.copy()
                for col in convert_date_columns:
                    dtype_dict[col] = 'object'

                df = pd.read_csv(url, sep=';', encoding='ISO-8859-1', dtype=dtype_dict, na_values=typesCVM.na_values)

                for col in convert_date_columns:
                    df[col] = pd.to_datetime(df[col], format='%Y-%m-%d')

                df.to_csv(file_path, index=False, sep=';', encoding='ISO-8859-1')
                print(f"File saved at: {file_path}")

            return df

        except requests.exceptions.RequestException as e:
            print(f"Error downloading the file: {e}")

        except pd.errors.ParserError as e:
            print(f"Error processing the CSV file: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")

        return None

    @staticmethod
    def build_inverted_index(dataframe: pd.DataFrame, column_name: str) -> dict:
        inverted_index = defaultdict(list)
        for idx, name in enumerate(dataframe[column_name]):
            words = name.split()
            for word in words:
                inverted_index[word.lower()].append(idx)
        return inverted_index

    @staticmethod
    def find_similar_names(input_text: str, dataframe: pd.DataFrame, keywords_present=[], limit=10) -> pd.DataFrame:
        pd.set_option('display.max_colwidth', None)
        input_words = input_text.lower().split()
        matches = []

        column_name: str = 'DENOM_SOCIAL'
        inverted_index: dict = FundNameSearch.build_inverted_index(dataframe, column_name)
        
        for word in input_words:
            if word in inverted_index:
                for idx in inverted_index[word]:
                    name = dataframe.iloc[idx][column_name]
                    score = fuzz.partial_ratio(input_text.lower(), name.lower())

                    for keyword_present in keywords_present:
                        if keyword_present.lower() in name.lower():
                            score += 20

                    keywords_found = sum(1 for p in keywords_present if p.lower() in name.lower())
                    score += keywords_found * 50

                    matches.append((name, idx, score))

        matches = sorted(matches, key=lambda x: x[2], reverse=True)[:limit]
        df_matches = pd.DataFrame(matches, columns=['Social Name', 'Index', 'Score'])

        df_matches['CNPJ'] = dataframe.loc[df_matches['Index'], 'CNPJ_FUNDO'].tolist()
        
        return df_matches

    @staticmethod
    def search_data_by_indices(original_df: pd.DataFrame, matches_df: pd.DataFrame) -> pd.DataFrame:
        selected_indices = matches_df['Index'].tolist()
        selected_df = original_df.iloc[selected_indices]
        return selected_df
