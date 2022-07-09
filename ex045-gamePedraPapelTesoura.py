#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print('Vamos jogar JOKENPÔ!')
print('')
print('''Escolha sua jogada:
[1] Pedra
[2] Papel
[3] Tesoura''')
opc = int(input('Opção escolhida: '))
cpu = randint(1, 3)
print('')
print('Vai!')
print('')
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
sleep(0.5)
print('')
if opc == 1 and cpu == 2:
    print(f'''Você: PEDRA
Eu: PAPEL

EU VENCI!''')
elif opc == 1 and cpu == 3:
    print(f'''Você: PEDRA
Eu: TESOURA
VOCÊ VENCEU!''')
elif opc == 2 and cpu == 1:
    print(f'''Você: PAPEL
Eu: PEDRA

VOCÊ VENCEU!''')
elif opc == 2 and cpu == 3:
    print(f'''Você: PAPEL
Eu: TESOURA

EU VENCI!''')
elif opc == 3 and cpu == 1:
    print(f'''Você: TESOURA
Eu: PEDRA

EU VENCI!''')
elif opc == 3 and cpu == 2:
    print(f'''Você: TESOURA
Eu: PAPEL

VOCÊ VENCEU!''')
else:
    print('EMPATE!')