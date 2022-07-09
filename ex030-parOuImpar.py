#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print(f'Você digitou o número {num} e ele é PAR!')
else:
    print(f'Você digitou o número {num} e ele é ÍMPAR!')