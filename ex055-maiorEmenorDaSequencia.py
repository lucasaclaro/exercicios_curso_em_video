#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lista = []
for c in range (1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa (kg): '))
    lista.append(peso)
maior = max(lista)
menor = min(lista)
print(f'O maior peso digitado foi {maior:.2f}kg e o menor foi {menor:.2f}kg.')