#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    opc = input('Quer continuar?[S/N]: ').upper().strip()[0]
    if opc == 'N':
        break
    elif opc not in 'SN':
        opc = input('Opção inválida. Quer continuar?[S/N]: ').upper().strip()[0]
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foram: {lista}.')
num5 = lista.count(5)
if num5 == 0:
    print('O número 5 não foi digitado.')
else:
    print(f'O número 5 foi digitado {num5} vez(es).')