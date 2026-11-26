'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = (
    "Flamengo","Palmeiras","Cruzeiro","Mirassol","Fluminense",
    "Botafogo","Bahia","São Paulo","Grêmio","Red Bull Bragantino",
    "Atlético-MG","Santos","Corinthians","Vasco da Gama","Vitória",
    "Internacional","Chapecoense","Coritiba","Athletico-PR","Remo",
)

print(f'Os 5 Primeiros Times são: {times[0:5]}')
print(f'Os 4 Ultimos Colocados são: [{times[-4:]}]')
print(f'Os times em orden Alfabetica e: {sorted(times)}')
print(f'O Time da Chapecoense esta na posição: {times.index("Chapecoense")+1} posição')