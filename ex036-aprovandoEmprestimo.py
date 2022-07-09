#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

cas = float(input('Qual o valor do imóvel: R$ '))
sal = float(input('Qual o salário do comprador: R$ '))
ano = int(input('Qual o total de anos do empréstimo: '))
par = cas / (ano * 12)
max = (sal * 30) / 100
if par > max:
    print(f'O empréstimo não foi aprovado. O valor da prestação é de no mínimo R${par:.2f}, o que excede os 30% do salário.')
else:
    print(f'O empréstimo foi aprovado. O valor da prestação é de no mínimo R${par:.2f}, o que não excede os 30% do salário.')