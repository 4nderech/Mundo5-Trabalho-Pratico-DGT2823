# Trabalho Prático | DGT2823 Tecnologias para desenv. de soluções de big data
# Dev Full Stack - Estacio
print("\nTrabalho Prático | DGT2823 Tecnologias para desenv. de soluções de big data")
print("Desenvolvimento Full Stack - Faculdade Estacio de Sa")

# Importar bibliotecas necessarias
import pandas as pd

# Ler o CSV (ajuste o caminho, separador e encoding se necessário)
df = pd.read_csv('dados.csv', sep=';', engine='python', encoding="utf-8")
print("\nDataframe Original e Informações Gerais pré-tratamento:")
print(df)
print(df.info())

# Criar variavel e atribuir a cópia do arquivo original
copy_df = df.copy()

# Corrigir valores na coluna 'Calories'
copy_df['Calories'] = copy_df['Calories'].astype(str).str.extract(r'(\d+)')
copy_df['Calories'] = pd.to_numeric(copy_df['Calories'], errors='coerce')
# Substituir valores ausentes em 'Calories' por 0
copy_df['Calories'] = copy_df['Calories'].fillna(0)

# Corrigir os valores da coluna 'Date'
copy_df['Date'] = copy_df['Date'].astype(str).str.replace("'", "")
# Substituir valores ausentes em 'Date'
copy_df['Date'] = copy_df['Date'].fillna('1900/01/01')
# Corrigir formato incorreto de datas ('20201226')
copy_df['Date'] = copy_df['Date'].replace('20201226', '2020/12/26')
# Converter coluna 'Date' para datetime
copy_df['Date'] = pd.to_datetime(copy_df['Date'], format='%Y/%m/%d', errors='coerce')

# Remover valores nulos restantes
copy_df = copy_df.dropna()

# Imprima o dataframe com os resultados já tratados
print("\nDataFrame final após tratamento dos dados:")
print(copy_df)

print("\nInformações Gerais do DataFrame Tratado:")
print(copy_df.info())