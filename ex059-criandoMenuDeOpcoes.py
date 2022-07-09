#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa ''')
opc = int(input('Opção: '))
print('')
print('*' * 25)
while opc != 5:
    if opc == 1:
        print(f'{num1:.2f} + {num2:.2f} = {num1 + num2}.')
        print('*' * 25)
    elif opc == 2:
        print(f'{num1:.2f} x {num2:.2f} = {num1 * num2}.')
        print('*' * 25)
    elif opc == 3:
        print(f'O maior valor entre {num1:.2f} e {num2:.2f} é {max(num1, num2)}.')
        print('*' * 25)
    elif opc ==4:
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segundo número: '))
        print('*' * 25)
    else:
        print('Opção inválida.')
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa ''')
    opc = int(input('Opção: '))
print('*' * 25)
print('Finalizando o programa...')
