#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
num = int(input('Digite um número inteiro entre 0 e 5: '))
lista = [0, 1, 2, 3, 4, 5]
sort = random.choice(lista)
print('Pensando...')
if num == sort:
    print(f'Você digitou {num} e eu escolhi {sort}. EU VENCI!')
else:
    print(f'Você digitou {num} e eu escolhi {sort}. VOCÊ VENCEU!')
