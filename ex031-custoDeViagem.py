#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dis = int(input('Digite a distância da viagem em km: '))
preU = dis * 0.5
preD = dis * 0.45
if dis <= 200:
    print(f'Em uma viagem de {dis}km, o seu preço total será de R${preU:.2f}.')
else:
    print(f'Em uma viagem de {dis}km, o seu preço total será de R${preD:.2f}.')

