#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
while cont < 10:
    print(termo, end = ' -> ')
    termo += razao
    cont += 1
print('Fim')