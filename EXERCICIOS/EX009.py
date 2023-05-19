#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input("Digite um número inteiro: "))

print("Tabuada do", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
