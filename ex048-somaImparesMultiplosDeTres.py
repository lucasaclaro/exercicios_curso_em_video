#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

lista = []
cont = 0
while cont < 500:
    if cont % 3 == 0 and cont % 2 != 0:
        lista.append(cont)
    cont +=1
print(f'Total de {len(lista)} números que somados resultam em {sum(lista)}.')
