from matplotlib import pyplot as plt

anos = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
vendas = [10, 15, 12, 18, 25, 33, 45]

# Cria um gráfico de linha com pontos em cada intersecção
plt.plot(anos, vendas, color='green', marker='o')

# Adiciona um título para o gráfico
plt.title('Quantidade de Casas Vendidas')

# Adiciona um título no eixo y e x
plt.ylabel('Qtd de Casas Vendidas')
plt.xlabel('Anos')

plt.show()
