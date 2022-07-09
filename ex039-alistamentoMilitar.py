#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = date.today().year
nas = int(input('Informe o ano de nascimento: '))
ali = ano - nas
anoC = nas + 18
if ali > 18:
    print(f'Você já deveria ter se alistado em {anoC}.')
elif ali < 18:
    print(f'Você ainda não tem idade para o alistamento, o qual deverá ser feito no ano de {anoC}.')
else:
    print('Esse é o ano do seu alistamento.')