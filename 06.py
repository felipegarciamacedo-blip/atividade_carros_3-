import pandas as pd

# 1. Carregar o arquivo CSV
df = pd.read_csv('carros.csv')
# 2. Agrupar por empresa e calcular a média da coluna 'average-mileage'
media_km = df.groupby('company')['average-mileage'].mean()

# 3. Exibir o resultado
print(media_km)