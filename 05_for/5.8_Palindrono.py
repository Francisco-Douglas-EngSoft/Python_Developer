'''Crie um programa que leia uma frase qualquer e diga se ela 
é um palíndromo, desconsiderando os espaços'''

frase = str(input("Digite a frase: ")).upper().strip()
f = frase.replace(" ", "")
inver = ''
for p in range(len(f) -1, -1, -1):
    inver += f[p]
    
print(f'Frase Original {f}')
print(f'Frase Inversa {inver}')

if f == inver:
    print('A palavra forma um palindromo')
else:
    print('A palavra não forma um palindrono')