#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
print(f'O aluno {nome} tirou {n1} na primeira prova e {n2} na segunda, obtendo como média final: {media:.1f}.')