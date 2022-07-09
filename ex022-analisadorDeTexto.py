#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ').strip()
nomeMa = nome.upper()
nomeMi = nome.lower()
nomeQdd = len(nome) - nome.count(' ')
nomeP = nome.split()[0]
print('')
print('Analisando o seu nome...')
print('')
print(f'O seu nome em letras maiúsculas é {nomeMa}.')
print(f'O seu nome em letras minúsculas é {nomeMi}.')
print(f'O seu nome possui {nomeQdd} letras.')
print(f'O seu primeiro nome é {nomeP}.')
