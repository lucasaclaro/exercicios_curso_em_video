#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cs = float(input('Digite a temperatura de graus Celsius: '))
fh = (cs * 9/5) + 32
print(f'A temperatura de {cs}ºC corresponde a {fh}ºF.')