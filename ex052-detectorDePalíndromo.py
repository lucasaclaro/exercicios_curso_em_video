#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
juntoC = junto[::-1]
if junto == juntoC:
    print(f'A frase digitada é um políndromo, uma vez que o inverso de {junto} é {juntoC}.')
else:
    print(f'A frase digitada não é um políndromo, uma vez que o inverso de {junto} não é {juntoC}.')