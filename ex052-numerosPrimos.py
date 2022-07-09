#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

lista = []
num = int(input('Digite um número para verificar se ele é primo: '))
if num == 0 or num == 1:
    print(f'O número {num} não é primo.')
else:
    for c in range(2, num + 1):
         res = num % c
         if num % c == 0:
            lista.append(num)
    if len(lista) == 1:
        print(f'O número {num} é primo.')
    elif len(lista) >= 2:
        print(f'O número {num} não é primo.')