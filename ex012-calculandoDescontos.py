#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

nome = input('Digite o nome do produto: ')
valor = float(input('Digite o preço do produto: R$'))
desc = (valor * 5) / 100
valorAt = valor - desc
print(f'O {nome} que custava o valor de R${valor}, com o desconto de 5% aplicado passará a custar R${valorAt:.2f}.')