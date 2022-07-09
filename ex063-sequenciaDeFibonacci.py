#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

seq = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
t3 = t1 + t2
while cont <= seq:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim')