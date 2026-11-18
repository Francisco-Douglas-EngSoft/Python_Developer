'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por 
Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distancia = float(input("Digite a Distancia em KM: "))

if distancia > 0:
    if distancia <= 20:
        custo = distancia * 0.50
    else:
        custo = distancia * 0.45
    print(f'Para uma Distancia de {distancia}km o custo sera de {custo}R$')
else:
    print('A Distancia precisa ser maior que 0')