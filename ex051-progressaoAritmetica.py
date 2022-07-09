#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

ter = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
print('')
print('Os 10 termos da razão acima são:')
for c in range (0, 10):
    print(ter, end = ' -> ')
    ter += raz
print('Fim')

