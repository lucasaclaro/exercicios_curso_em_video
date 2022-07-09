#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.


times = ('São Paulo', 'Palmeiras', 'Corinthians', 'Santos', 'Flamengo', 'Vasco', 'Fluminense',
         'Bahia', 'Vitória', 'Atlético/Mg', 'Cruzeiro', 'Chapecoense', 'Ferroviária',
         'Guarani', 'Ponte Preta', 'Grêmio', 'Internacional', 'Juventude', 'Atlético/Pr', 'RedBull')
print(f'Os cinco primeiros times do Campeonato Brasileiro são: {times[0:5]}.')
print(f'Os quatro últimos times do Campeonato Brasileiro são: {times[(len(times) - 4):len(times)]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f"A Chapecoense está na posição {times.index('Chapecoense') + 1}.")