#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

num = 0
while num >= 0:
    num = int(input('Digite um número para que seja exibida a sua tabuada: '))
    cont = 0
    while cont <= 10:
        print(f'{num} x {cont} = {cont * num}')
        cont += 1
print('Programa encerrado.')