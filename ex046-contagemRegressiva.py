#Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

cont = 10
while cont >= 0:
    print(f'{cont}!')
    sleep(1)
    cont -= 1
print('BOOMMM!!')

