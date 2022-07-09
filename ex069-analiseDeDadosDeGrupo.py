#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

listaId = []
contId = 0
listaH = []
contH = 0
listaM = []
contM = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M / F]: ').upper().strip()[0]
    if idade > 18:
        contId += 1
        listaId.append(contId)
    if sexo == 'M':
        contH += 1
        listaH.append(contH)
    if idade < 20 and sexo == 'F':
        contM += 1
        listaM.append(contM)
    print('**' * 15)
    print('')
    opc = input('Quer continuar [S / N]: ').upper().strip()[0]
    print('')
    if opc == 'N':
        break
print(f'Foi(aram) digitada(s) {len(listaId)} pessoa(s) com mais de 18 anos.')
print(f'Foi(aram) digitada(a) {len(listaH)} pessoa(s) do sexo masculino.')
print(f'Foi(aram) digitada(s) {len(listaM)} pessoa(a) do sexo feminino com menos de 20 anos.')