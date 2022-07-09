#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
listaP = []
listaI = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    if num % 2 == 0:
        listaP.append(num)
    else: listaI.append(num)
    opc = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if opc not in 'SN':
        opc = input('Opção inválida. Quer continuar? [S/N]: ')
    if opc == 'N':
        break
print(f'Lista geral: {lista}.')
print(f'Lista de números pares: {listaP}.')
print(f'Lista de números ímpares: {listaI}.')
