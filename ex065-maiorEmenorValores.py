#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

lista = []
opc = 'S'
while opc == 'S':
    num = int(input('Digite um número inteiro: '))
    lista.append(num)
    opc = input('Quer continuar? [S/N]: ').upper().strip()[0]
print(f'Você digitou {len(lista)} valores, sendo que a média entre eles é {sum(lista) / len(lista)}, o maior valor é {max(lista)} e o menor é {min(lista)}.')