#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.73,
            'Borracha', 2.45,
            'Papel', 3.55,
            'Caderno', 15.85,
            'Lapiseira', 6.58,
            'Apontador', 3.55)
print('Lista de preços')
print('')
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<9}',end='')
        print('................ R$ ', end='')
    if pos % 2 == 1:
        print(f'{produtos[pos]:>7}')

