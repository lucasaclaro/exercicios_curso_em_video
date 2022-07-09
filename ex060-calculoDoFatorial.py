#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite um número para que eu calcule o seu fatorial: '))
cont = num
fat = 1
print(f'{num}! = ', end='')
while num >= 1:
    print(f'{num}', end='')
    print(' x ' if num > 1 else ' = ', end='')
    fat *= num
    num -=1
print(fat)