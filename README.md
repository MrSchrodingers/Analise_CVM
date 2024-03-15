
# Análise de Fundos de Investimento 

Os fundos de investimento são veículos de investimento coletivo que reúnem o capital de vários investidores para serem gerenciados por profissionais financeiros. Eles investem em uma variedade de ativos, como ações, títulos, commodities, imóveis e outros instrumentos financeiros, com o objetivo de alcançar retornos para os investidores.

Os fundos de investimento são administrados por instituições financeiras, como bancos, corretoras ou gestoras de recursos. Cada fundo possui um objetivo de investimento específico e uma estratégia de alocação de ativos definida, o que pode variar de fundo para fundo.

## CVM - Comissão de Valores Mobiliários

A Comissão de Valores Mobiliários (CVM) é uma entidade autárquica vinculada ao Ministério da Economia do Brasil, responsável por regular e fiscalizar o mercado de valores mobiliários no país. Ela tem como objetivo principal proteger os investidores e promover o desenvolvimento saudável do mercado de capitais.

Entre as suas atribuições, a CVM regulamenta a constituição e funcionamento dos fundos de investimento, estabelecendo regras e diretrizes para sua operação. Ela também é responsável por fiscalizar e supervisionar as atividades das instituições financeiras que atuam nesse mercado, garantindo a transparência e a integridade das operações.





## Manual do Usuário

[Em produção]

#### main.py: O ponto de entrada do programa. Ele interage com o usuário e chama as funções relevantes para realizar as operações de busca e análise de dados.
#### BuscaFundosCNPJ.py e BuscaFundosNome.py: Módulos que contêm classes para buscar fundos por CNPJ ou por nome, respectivamente.
#### Rendimento.py: Um módulo para calcular o rendimento de fundos de investimento.
#### CadastroCVM/: Um diretório contendo arquivos e módulos relacionados ao cadastro de fundos de investimento, como extração de dados e definição de tipos.
#### InfoFundo/: Um diretório onde os dados dos fundos de investimento são salvos como arquivos CSV.
## Funcionalidades

[Atuais]

Este é um programa Python desenvolvido para facilitar a busca e análise de informações sobre Fundos de Investimento. Ele oferece funcionalidades para buscar fundos por CNPJ ou por nome, extrair dados sobre esses fundos e salvar os resultados em arquivos CSV para posterior análise.

Busca de fundos por CNPJ ou nome.
    Extração de dados sobre os fundos encontrados.
    Salvamento dos dados em arquivos CSV para análise posterior.


## Instalação

Clone o repositório do GitHub para sua máquina local.
```bash
git clone https://github.com/MrSchrodingers/Analise_CVM.git
```

Navegue até o diretório do projeto.

```bash
cd Analise_CVM
```

Execute o programa.

```bash
python AnaliseFundos.py
```

Siga as instruções exibidas no terminal para buscar informações sobre fundos de investimento.
## Uso/Exemplos

#### Buscar um fundo por CNPJ:
```bash
Do you want to search for the Investment Fund by CNPJ or Name? cnpj
Enter the CNPJ of the Investment Fund: 28.280.995/0001-00
Enter the start year: 2020
Enter the end year: 2022
```

#### Buscar um fundo por nome:
```bash
Do you want to search for the Investment Fund by CNPJ or Name? name
Enter the Name of the Investment Fund: Fundo XYZ
Enter the keywords for the Investment Fund: income, balanced
```
## Contribuindo

Contribuições são sempre bem-vindas!


## Autores

- <img src="https://github.com/MrSchrodingers/Analise_CVM/assets/69037408/d8551934-e45f-4185-a57a-220e20afc5a8" height="18" width="18"/> [@MrSchrodingers](https://www.github.com/MrSchrodingers) 

