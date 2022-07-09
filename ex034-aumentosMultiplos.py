#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o salario do colaborador: R$ '))
if sal > 1250:
    aum = (sal * 10) / 100
    tot = sal + aum
    print(f'Com o aumento salarial, a remuneração foi para R$ {tot:.2f}.')
else:
    aum = (sal * 15) / 100
    tot = sal + aum
    print(f'Com o aumento salarial, a remuneração foi para R$ {tot:.2f}.')