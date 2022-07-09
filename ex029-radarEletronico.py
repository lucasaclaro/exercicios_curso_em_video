#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Digite a velocidade: '))
if vel > 80:
    print('Você foi multado!')
    mul = vel - 80
    val = mul * 7
    print(f'O valor da multa é de R${val:.2f}.')
else:
    print('Parabéns, você não ultrapassou o limite de velocidade. Dirija com segurança.')