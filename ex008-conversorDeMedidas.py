#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input('Digite um valor em metro(s): '))
cm = valor * 100
mm = valor * 1000
print(f'Você digitou o valor de {valor}m, o qual corresponde à {cm:.0f}cm e {mm:.0f}mm.')