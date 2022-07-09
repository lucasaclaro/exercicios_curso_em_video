#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append((num))
    else:
        num = int(input('O valor já foi digitado anteriormente, digite outro número: '))
        lista.append((num))
    opc = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if opc == 'N':
        break
lista.sort()
print(f'Os valores digitados foram: {lista}')