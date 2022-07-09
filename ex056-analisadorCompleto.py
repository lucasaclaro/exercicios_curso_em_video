#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

totIdade = 0
men20 = 0
nomeV = 0
idadeV = 0
for c in range(1, 5):
    nome = input(f'Digite o nome da {c}ª pessoa: ')
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = input(f'Digite sexo da {c}ª pessoa [M / F]: ').upper().strip()
    print('')
    totIdade += idade
    if idade < 20 and sexo == 'F':
        men20 += 1
    if sexo == 'M' and idade > idadeV:
        idadeV = idade
        nomeV = nome
mediaIdade = totIdade / 4
print(f'Média de idade do grupo: {mediaIdade}.')
print(f'Mulheres com menos de 20 anos: {men20}.')
print(f'Nome do homem mais velho e sua idade: {nomeV}, {idadeV} anos.')