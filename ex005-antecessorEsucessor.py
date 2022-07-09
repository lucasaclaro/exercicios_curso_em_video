#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número inteiro: '))
suc = num + 1
ant = num - 1
print(f'Você digitou o número {num}, sendo que o seu sucessor é {suc} e o seu antecessor é {ant}.')