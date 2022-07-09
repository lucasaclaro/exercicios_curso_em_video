#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}.')
elif num2 > num1:
    print(f'{num2} é maior que {num1}.')
else:
    print(f'{num1} é igual {num2}.')
