'''Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.'''

'''Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.'''

'''Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.'''

maior = 0
menor = 0

for p in range(1, 6):
    nome = input(f'Nome da {p}ª pessoa: ')
    peso = float(input(f'Peso de {nome}: '))

    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'\nO maior peso foi {maior:.1f} kg')
print(f'O menor peso foi {menor:.1f} kg') 
    