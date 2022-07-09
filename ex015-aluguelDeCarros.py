#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de quilômetros percorridos com o veículo: '))
dia = int(input('Digite a quantidade de dias que o veículo foi alugado: '))
precoKm = km * 0.15
precoDia = dia * 60
preco = precoKm + precoDia
print(f'O valor total a ser pago pelo aluguel do veículo é de R${preco:.2f}.')