#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Informe a temperatura em celsius:'))
fahrenheit = temp * 1.8 + 32
print('Sua temperatura convertida em Fahrenheit é {}'.format(fahrenheit))