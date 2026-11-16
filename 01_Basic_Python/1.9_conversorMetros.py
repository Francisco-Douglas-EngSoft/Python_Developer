# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Digite o valor em metros: "))
# Converte metros em Decametros, Hectômetros e Quilômetros
decam = metros / 10
hect = metros / 100
qm = metros / 1000

# Converte metros em Decímetros, Centímetros e Milímetros
dec = metros * 10
cent = metros * 100
mil = metros * 1000

print(f"{metros} metros equivalem a:")
print(f"{decam} decametros")
print(f"{hect} hectometros")
print(f"{qm} quilometros")
print(f"{dec} decimetros")
print(f"{cent} centimetros")
print(f"{mil} milimetros")
