#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n1= float(input('Quanto de dinheiro você tem na carteira: '))

cambio = n1 / 5.16

print('Com esse valor você consegue comprar {:.2f} dolares'.format(cambio))