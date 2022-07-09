#Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

lista = []
num = 0
while num <= 50:
    if num % 2 == 0:
        lista.append(num)
    num += 1
print(lista)
print('Acabou')