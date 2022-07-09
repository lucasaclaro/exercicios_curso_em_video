#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

tot = mais = menor = 0
maisB = ''
cont = 0
while True:
    prodt = input('Produto: ')
    preco = float(input('Preço: R$ '))
    cont += 1
    tot += preco
    if preco > 1000:
        mais += 1
    if cont == 1:
        menor = preco
        maisB = prodt
    else:
        if preco < menor:
            menor = preco
            maisB = prodt
#    if preco < menor:
#        menor = preco
#        maisB = prodt
    opc = input('Quer continuar? [S / N]: ').upper().strip()[0]
    print('')
    if opc == 'N':
        break
print(f'Valor total da compra: R$ {tot:.2f}.')
print(f'{mais} produto(s) custa(m) mais de R$ 1000.00.')
print(f'O produto mais barato é o {maisB}, custando R$ {menor:.2f}.')

