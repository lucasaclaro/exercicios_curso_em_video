#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite o seu nome: ').upper()
if 'SILVA' not in nome:
    print('O nome digitado NÃO contém SILVA.')
else:
    print('O nome digitado contém SIM a palavra SILVA.')
