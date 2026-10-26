import pandas as pd

# 1. Carregar o arquivo CSV
df = pd.read_csv('carros.csv')

# 2. Filtrar apenas os carros da empresa Toyota
toyota_cars = df[df['company'] == 'toyota']

# 3. Imprimir os detalhes
print(toyota_cars)