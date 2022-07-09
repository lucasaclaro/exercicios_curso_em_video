#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('Vamos jogar PAR ou ÍMPAR!')
lista1 = []
cont1 = 0
lista2 = []
cont2 = 0
while len(lista2) == 0:
    jog = int(input('Escolha um número: '))
    cpu = randint(0, 10)
    opc = int(input('[1] PAR  /  [2] ÍMPAR: '))
    res = jog + cpu
    if opc == 1 and res % 2 == 0:
         print(f'{jog} + {cpu} = {res}. É PAR! Você GANHOU!')
         cont1 += 1
         lista1.append(cont1)
    elif opc == 1 and res % 2 != 0:
        print(f'{jog} + {cpu} = {res}. É ÍMPAR. Eu GANHEI!')
        cont2 += 1
        lista2.append(cont2)
    elif opc == 2 and res % 2 == 0:
         print(f'{jog} + {cpu} = {res}. É PAR! Eu GANHEI!')
         cont2 += 1
         lista2.append(cont2)
    elif opc == 2 and res % 2 != 0:
        print(f'{jog} + {cpu} = {res}. É ÍMPAR. Você GANHOU!')
        cont1 += 1
        lista1.append(cont1)
print(f'Você teve {len(lista1)} vitórias consecutivas!')


