#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('Tratando valores')
print('')
num = 0
cont = 0
soma = 0
while num != 999:
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
    cont += 1
print(f'Foram digitados {cont - 1} valores, sendo que a soma deles foi {soma}.')

