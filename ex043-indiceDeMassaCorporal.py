#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

print('Calculadora de IMC')
print('')
pes = float(input('Digite o peso (kg): '))
alt = float(input('Digite a altura (cm): '))
imc = pes / (alt ** 2)
print('**' * 20)
print(f'O seu índice de massa corporal é: {imc:.2f}, portanto você está na faixa abaixo: ')
if imc < 18.5:
    print('IMC abaixo de 18,5: Abaixo do Peso')
elif imc < 25:
    print('Entre 18,5 e 25: Peso Ideal')
elif imc < 30:
    print('25 até 30: Sobrepeso')
elif imc < 40:
    print('30 até 40: Obesidade')
else:
    print('Acima de 40: Obesidade Mórbida')