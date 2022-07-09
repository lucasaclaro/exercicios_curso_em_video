#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite o sexo da pessoa [M / F]: ').strip().upper()
while sexo != 'M' and sexo != 'F':
    print("Valor inválido. Somente são aceitos 'M' (masculino) e 'F' (feminino).")
    sexo = input('Digite o sexo da pessoa [M / F]: ').strip().upper()
print('Dado armazenado.')

