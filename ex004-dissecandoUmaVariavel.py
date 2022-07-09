#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

verificar = input('Digite algo para que eu verifique o seu tipo primitivo: ')
tipo = type(verificar)
print(f'Você digitou "{verificar}", e o seu tipo primitivo é "{tipo}".')

#Uma vez que topo valor em um imput retorna uma string, o comando abaixo irá verificar se é um número:

print(f'Você digitou {verificar}, isso é um número?: {verificar.isnumeric()}')

