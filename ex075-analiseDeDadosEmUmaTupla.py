#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.


num = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'Números digitados: {num}.')
print(f'O número 9 aparece {num.count(9)} vez(es).')
if 3 in num:
    print(f'O número 3 foi digitado na posição {num.index(3) + 1}.')
else:
    print('O número 3 não foi digitado.')
print(f'Os números pares digitados foram: ', end = '')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')