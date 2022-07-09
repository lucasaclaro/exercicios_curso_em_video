#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
tinta = area / 2
print(f'''A parede digitada possui {lar:.2f}m de largura e {alt:.2f} de altura, o que corresponde a uma área total de {area}m².
Dessa maneira, para pintar essa parede será necessário a quantidade de {tinta} litro(s) de tinta.''')
