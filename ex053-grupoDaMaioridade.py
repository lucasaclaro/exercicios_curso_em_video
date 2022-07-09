#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano = date.today().year
cont = 0
for c in range (1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if ano - nasc >= 18:
        print(f'Atingiu a maioridade em {ano}!')
        cont += 1
    else:
        print(f'Não atingiu a maioridade em {ano}!')
    print('')
print('')
print(f'{cont} das 7 pessoas acima atingiram a maioridade em {ano}.')