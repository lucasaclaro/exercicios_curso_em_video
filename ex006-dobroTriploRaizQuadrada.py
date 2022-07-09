#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

num = int(input('Digite um número inteiro: '))
dobro = num * 2
triplo = num * 3
raizq = sqrt(num)
print(f'Você digitou o número {num}, sendo que o dobro dele é {dobro}, o triplo é {triplo} e a raiz quadrada é {raizq}.')

