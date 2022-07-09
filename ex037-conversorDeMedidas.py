#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
import math
num = int(input('Digite um número inteiro: '))
bina = bin(num)[2:]
octa = oct(num)[2:]
hexa = hex(num)[2:]
print('~~' * 15)
print('''[A] Binário
[B] Octal
[C] Hexadecimal
''')
opc = input('Digite a opção desejada: ').strip().upper()
if opc == 'A':
    print(f'O valor em binário é {bina}.')
elif opc == 'B':
    print(f'O valor em octal é {octa}.')
elif opc == 'C':
    print(f'O valoe em hexadecinal é {hexa}.')
else:
    print('Opção digitada inválida.')


