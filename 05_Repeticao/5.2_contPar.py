''' Crie um programa que mostre na tela todos os números 
pares que estão no intervalo entre 1 e 50.'''

contPar = 0

for n in range(1, 50):
    if n % 2 == 0:
        contPar += 1
        print(f'{n}', end=" ")
    else:
        pass
print('Fim')