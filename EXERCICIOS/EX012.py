#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Digite o preço do produto : '))
desconto = (5/100) * produto
valor_final = produto - desconto

print(('O valor final do seu produto é {} reais.'.format(valor_final)))