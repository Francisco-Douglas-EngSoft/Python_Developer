'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''


p = int(input('Primeiro termo: '))
r = int(input('Razao: '))
termo = p
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += r
    cont += 1
    