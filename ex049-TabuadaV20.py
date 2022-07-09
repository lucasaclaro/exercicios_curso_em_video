#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input("Digite um número para que eu exiba a tabuada dele: "))
cont = 0
print('')
print(f'Tabuada do {num}:')
print('')
print('~' * 15)
for c in range(0, 11):
    print(f'{cont} x {num} = {cont * num}')
    cont +=1
print('~' * 15)
print('Fim')