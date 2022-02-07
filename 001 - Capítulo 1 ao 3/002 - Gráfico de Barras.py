from matplotlib import pyplot as plt

vendas = (15, 40, 24, 28, 12)

index = [0, 1, 2, 3, 4]

plt.xticks(index, ('Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5'))

# Plota o gráfico de barras
bar = plt.bar(index, vendas)

# Adiciona um título para o gráfico
plt.title('Quantidade de Carros Vendidos por Dia')

# Adiciona um título no eixo y e x
plt.ylabel('Qtd de Carros')

plt.show()
