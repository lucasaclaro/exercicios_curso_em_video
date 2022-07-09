#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
lista = [num1, num2, num3]
max = max(lista)
min = min(lista)
print(f'O valor máximo digitado foi {max:.2f} e o mínimo foi {min:.2f}.')

