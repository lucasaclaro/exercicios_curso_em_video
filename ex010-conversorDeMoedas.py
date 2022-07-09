#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Cotação do dólar em 10/05/2022 = R$ 5,16

real = float(input(f'Digite quantos reais você tem na carteira: '))
dolar = real / 5.16
print(f'Você possui R${real:.2f}, o que corresponde a US${dolar:.2f}.')
