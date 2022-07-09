#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

num = num1 = int(input('Qual o valor do saque? R$ '))
ced100 = ced50 = ced20 = ced10 = ced5 = ced2 = ced1 = 0
while num >= 100:
    num = num - 100
    ced100 += 1
while num >= 50:
    num = num - 50
    ced50 += 1
while num >= 20:
    num = num - 20
    ced20 += 1
while num >= 10:
    num = num - 10
    ced10 += 1
while num >= 5:
    num = num - 5
    ced5 += 1
while num >= 2:
    num = num - 2
    ced2 += 1
while num >= 1:
    num = num - 1
    ced1 += 1
print(f'Para efetuar o saque de R$ {num1} foi(aram) necessaria(aram):')
if ced1 > 0:
    print(f'Cédula(s) de R$ 1 = {ced1}')
if ced2 > 0:
    print(f'Cédula(s) de R$ 2 = {ced2}')
if ced5 > 0:
    print(f'Cédula(s) de R$ 5 = {ced5}')
if ced10 > 0:
    print(f'Cédula(s) de R$ 10 = {ced10}')
if ced20 > 0:
    print(f'Cédula(s) de R$ 20 = {ced20}')
if ced50 > 0:
    print(f'Cédula(s) de R$ 50 = {ced50}')
if ced100 > 0:
    print(f'Cédula(s) de R$ 100 = {ced100}')



