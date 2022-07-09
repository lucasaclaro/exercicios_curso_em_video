#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

print('Digite os lados do triângulo a ser analisado:')
print('')
lad1 = float(input('Lado 1: '))
lad2 = float(input('Lado 2: '))
lad3 = float(input('Lado 3: '))
if lad1 + lad2 > lad3 and lad1 + lad3 > lad2 and lad2 + lad3 > lad1:
    if lad1 == lad2 == lad3:
        print('Os lados digitados formam um triângulo equilátero.')
    elif lad1 != lad2 != lad3 and lad1 != lad3:
        print('Os lados digitados formam um triângulo escaleno.')
    else:
        print('Os lados digitados formam um triângulo isósceles.')
else:
    print('Os lados digitados não formam um triângulo.')
