import pandas as pd

# 1. Carregar o arquivo CSV
df = pd.read_csv('carros.csv')

# 2. Contar a quantidade de carros por empresa
total_por_empresa = df['company'].value_counts()

# 3. Exibir o resultado
print(total_por_empresa)