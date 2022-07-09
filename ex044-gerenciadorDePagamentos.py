#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

pro = float(input('Digite o valor do produto: R$ '))
din = pro - (pro * 10 / 100)
car = pro - (pro * 5 / 100)
ca3 = pro + (pro * 20 / 100)
print('''Qual a forma de pagamento: 
[1] à vista no dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão''')
opc = int(input('Digite a opção escolhida: '))
print('')
if opc == 1:
    print(f'O valor a ser pago pelo produto, com o desconto aplicado é R$ {din:.2f}.')
elif opc == 2:
    print(f'O valor a ser pago pelo produto, com o desconto aplicado é R$ {car:.2f}.')
elif opc == 3:
    print(f'Valor normal do produto: {pro:.2f}.')
elif opc == 4:
    print(f'O valor a ser pago pelo produto, com os juros aplicados é R$ {ca3:.2f}.')
else:
    print('Opção inválida.')