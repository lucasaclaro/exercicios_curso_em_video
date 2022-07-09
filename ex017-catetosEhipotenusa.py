#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co, ca)
print(f'Em um triângulo retângulo onde o cateto oposto corresponde a {co} e o cateto adjacente a {ca}, o valor da hipotenusa é {hip:.2f}. ')