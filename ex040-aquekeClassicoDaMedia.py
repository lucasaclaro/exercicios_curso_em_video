#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

not1 = float(input('Digite a primeira nota: '))
not2 = float(input('Digite a segunda nota: '))
media = (not1 + not2) / 2
print(f'A sua média foi {media:.1f}:')
if media < 5:
    print('Reprovado.')
elif media >= 7:
    print('Aprovado.')
else:
    print('Recuperação.')