#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('PROGRAMAR', 'ESTUDAR', 'LEITURA', 'PYTHON')
for palavra in palavras:
    print(palavra, '', end='')
    print('possui as seguintes vogais: ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra,'', end='')
    print('')
