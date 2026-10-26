import pandas as pd

# 1. Carregar a planilha original
df = pd.read_csv('carros.csv')  # ou pd.read_excel('seu_arquivo.xlsx')

# 2. Limpeza dos dados
# Remove linhas com valores nulos/em branco
df_limpo = df.dropna()

# Remove linhas duplicadas (se houver)
df_limpo = df_limpo.drop_duplicates()

# 3. Salvar o conjunto de dados limpo em um novo arquivo CSV
df_limpo.to_csv('conjunto_de_dados_limpo.csv', index=False)

print("Dados limpos e salvos com sucesso!")