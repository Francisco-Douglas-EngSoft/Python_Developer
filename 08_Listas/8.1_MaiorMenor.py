'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

listaN = []

for n in range(1, 6):
    numeros = int(input(f'Digite o {n} numero: '))
    listaN.append(numeros)
    
print(f'A lista de numeros e {listaN}')
print(f'O Maior numero e {max(listaN)} na posição {listaN.index(max(listaN))+1}')
print(f'O Menor numero e {min(listaN)} na posição {listaN.index(min(listaN))+1}')