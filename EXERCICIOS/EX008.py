#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input('Digite o valor em metros que vc quer converter em centimetros e milimetros: '))
cm = n1 * 100
mm = n1 * 1000

print('Centimetros {:.2f} e milimetros {:.2f}'.format(cm, mm))
