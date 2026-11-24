'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado 
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print("Caixa eletrônico")

saque = int(input("Digite o valor que deseja sacar: R$ "))
valorOriginal = saque

cedulas = [50, 20, 10, 1]
quantidades = {}

for cedula in cedulas:
    quantidades[cedula] = saque // cedula
    saque %= cedula

if saque != 0:
    print("Não foi possível realizar o saque.")
else:
    print(f"\nSaque de R$ {valorOriginal}")

    for cedula in cedulas:
        if quantidades[cedula] > 0:
            print(
                f"{quantidades[cedula]} cédula(s) de R$ {cedula}"
            )