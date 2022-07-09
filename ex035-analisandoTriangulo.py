#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

seg1 = float(input('Digite o tamanho do primeiro segmento: '))
seg2 = float(input('Digite o tamanho do segundo segmento: '))
seg3 = float(input('Digite o tamanho do terceiro segmento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('Os valores digitados formam um triângulo.')
else:
    print('Os valores digitados não formam um triângulo.')
