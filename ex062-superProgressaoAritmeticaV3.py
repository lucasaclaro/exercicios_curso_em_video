#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
tot = 0
while cont < 10:
    tot += 1
    print(termo, end=' -> ')
    cont += 1
    termo += razao
print('Fim')
opc = 1
while opc != 0:
    opc = int(input('Quantos termos mais você quer que eu mostre? '))
    cont = 0
    while cont < opc:
        tot += 1
        print(termo, end=' -> ')
        cont += 1
        termo += razao
    print('Fim')
print('')
print(f'Programa encerrado com {tot} termos exibidos.')
