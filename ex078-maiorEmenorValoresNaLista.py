#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
for n in range (0,5):
    num = int(input(f'Digite um número na posição {n}: '))
    numeros.append(num)
print(f'O maior valor digitado foi {max(numeros)} e ele aparece na(s) posição(es): ', end='')
for i, v in enumerate(numeros):
    if v == max(numeros):
        print(i, ' . ', end='')
print('')
print(f'O menor valor digitado foi {min(numeros)} e ele aparece na(s) posição(es): ', end='')
for i, v in enumerate(numeros):
    if v == min(numeros):
        print(i, ' . ', end='')
print('')
print('Fim')
