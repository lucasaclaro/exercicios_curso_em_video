#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date
ano = date.today().year
anoN = int(input('Digite o ano de nascimento do atleta: '))
idade = ano - anoN
print(f'O atleta tem {idade} anos e pertence à categoria:')
if idade <= 9:
    print('Mirim.')
elif idade <= 14:
    print('Infantil.')
elif idade <= 19:
    print('Júnior.')
elif idade <= 25:
    print('Sênior.')
else:
    print('Master.')