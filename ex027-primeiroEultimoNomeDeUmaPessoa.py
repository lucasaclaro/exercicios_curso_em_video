#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.


nome = input('Digite o seu nome completo: ').strip()
nomeC = nome.split()
pNo = print(nomeC[0])
uNo = nomeC[len(nomeC) - 1]
print(f'O primeiro nome é {pNo}.')
print(f'O último nome é {uNo}.')

