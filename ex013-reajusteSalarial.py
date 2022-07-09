#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = input('Digite o nome do funcionário: ')
salario = float(input(f'Digite o salário do funcionário {nome}: '))
aumento = (salario * 15) / 100
salarioAt = salario + aumento
print(f'O salário do funcionário {nome} que era de R${salario:.2f}, com o aumento de 15%, passará a ser de R${salarioAt:.2f}.')