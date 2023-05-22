#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe seu salario: '))
porcentagem = (15/100)*salario
salario_final = salario + porcentagem
print('Seu novo salario é : {} '.format(salario_final))