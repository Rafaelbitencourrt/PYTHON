#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

qtd_km = float(input('Digite a quantidade de kilometros percorridos: '))
qtd_dias = int((input('Digite a quantidade de dias : ')))
preco = (qtd_dias * 60) + (qtd_km * 0.15)

print('O valor final é {}, pois vc percorreu {} km e ficou {} dias.'.format(preco, qtd_km, qtd_dias))

