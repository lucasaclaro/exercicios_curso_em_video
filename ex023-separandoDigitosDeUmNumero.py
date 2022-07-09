#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = str(input('Digite um número: ')).strip()
numS = len(num)
if numS > 0 and numS <2:
    print(f'Unidade: {num[0]}.')
elif numS > 1 and numS < 3:
    print(f'Unidade: {num[0]}.')
    print(f'Dezena: {num[1]}.')
elif numS > 2 and numS <4:
    print(f'Unidade: {num[0]}.')
    print(f'Dezena: {num[1]}.')
    print(f'Centena: {num[2]}.')
elif numS > 3 and numS <5:
    print(f'Unidade: {num[0]}.')
    print(f'Dezena: {num[1]}.')
    print(f'Centena: {num[2]}.')
    print(f'Milhar: {num[3]}.')
else:
    print('O número digitado não está entre os parâmetros: entre 0 e 9999.')

