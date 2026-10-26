import pandas as pd

# 1. Carregar o arquivo
df = pd.read_csv('carros.csv')

# 2. Filtrar a linha onde o preço é igual ao preço máximo do dataset
carro_mais_caro = df[['company', 'price']][df.price == df['price'].max()]

# 3. Exibir o resultado
print(carro_mais_caro)
