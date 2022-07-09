#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cid = input('Digite o nome de uma cidade: ').strip().upper()
cidS = cid.split()
if cidS[0] == 'SANTO':
    print('A cidade que você digitou começa SIM com a palavra SANTO.')
else:
    print('A cidade que você digitou NÃO começa com a palavra SANTO.')
