from CadastroCVM import BuscaFundosCNPJ, BuscaFundosNome
from Rendimento import CalculoRendimento
from typing import Union

import os

def save_dataframe_as_csv(data, cnpj):
    save_dir = 'InfoFundo'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    cnpj_file_name = cnpj.replace('/', '_')
    csv_file_name = os.path.join(save_dir, f'Fundo_{cnpj_file_name}.csv')

    data.to_csv(csv_file_name, index=False)
    print(f"DataFrame saved as CSV: {csv_file_name}")
    
def main() -> None:
    busca_fundos_cnpj = BuscaFundosCNPJ.FundSearch()
    busca_fundos_nome = BuscaFundosNome.FundNameSearch()

    flag_busca = input('Do you want to search for the Investment Fund by CNPJ or Name? ').lower()

    if flag_busca == 'cnpj':
        cnpj = input('Enter the CNPJ of the Investment Fund: ')
        start_year = int(input('Enter the start year: '))
        end_year = int(input('Enter the end year: '))

        data = busca_fundos_cnpj.extract_data_by_cnpj(cnpj, start_year, end_year)
        print(data)

        save_dataframe_as_csv(data, cnpj)

    elif flag_busca == 'name':
        database_CVM = busca_fundos_nome.search_cvm_registration()
        nome = input('Enter the Name of the Investment Fund: ')
        keywords = input('Enter the keywords for the Investment Fund: ')
        df = busca_fundos_nome.find_similar_names(nome, database_CVM, keywords_present=keywords)
        print(df)

        flag_busca_encontrada = input('Encontrou o CNPJ/ FI? ').lower()

        if flag_busca_encontrada == 'sim' or flag_busca_encontrada == 's':
            cnpj = input('Enter the CNPJ of the Investment Fund: ')
            start_year = int(input('Enter the start year: '))
            end_year = int(input('Enter the end year: '))

            data = busca_fundos_cnpj.extract_data_by_cnpj(cnpj, start_year, end_year)
            print(data)

            save_dataframe_as_csv(data, cnpj)
        else:
            database_CVM = busca_fundos_nome.search_cvm_registration()
            nome = input('Enter the Name of the Investment Fund: ')
            keywords = input('Enter the keywords for the Investment Fund: ')
            df = busca_fundos_nome.find_similar_names(nome, database_CVM, keywords_present=keywords)
            print(df)

    else:
        print('Invalid Option!')

if __name__ == "__main__":
    main()