# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.

dinheiro = float(input("Digite quanto dinheiro você tem na carteira: R$ "))
dolar = dinheiro / 5.25  # Supondo que a cotação do dólar seja R$ 5,25

print(f"Com R$ {dinheiro:.2f}, você pode comprar US$ {dolar:.2f}.")