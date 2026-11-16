# Faça um programa que leia um número
# Inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input("Digite um número para ver sua tabuada: "))

for n in range(1, 11):
    resultado = numero * n
    print(f"{numero} x {n} = {resultado}")