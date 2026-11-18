'''Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo 
que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input("Digite a velocidade do carro km: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Para quem ultrapassou {velocidade - 80} alem dos 80KM')
    print(f'Sera Multado em {multa}R$')
else:
    print(f'Para velocidade {velocidade}Km não tem multa')