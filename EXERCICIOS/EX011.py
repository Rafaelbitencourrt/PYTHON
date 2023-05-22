#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
area = altura * largura
litro = 2
qtd = area / litro
print('Area total informada: {:.2f} metros², você precisa de um total de {:.0f} latas de tintas.'.format(area, qtd))
