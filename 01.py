import pandas as pd

# 1. Carregar o arquivo da planilha
df = pd.read_csv('carros.csv')

# 2. Exibir as primeiras 5 linhas
print("=== PRIMEIRAS 5 LINHAS ===")
print(df.head(5))

#3. exibir as 5 ultimas
print("=== ULTIMAS 5 LINHAS===")
print(df.tail(5))