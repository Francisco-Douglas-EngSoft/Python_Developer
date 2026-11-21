'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''


p = int(input('Primeiro termo: '))
z = int(input('Razão: '))
d = p + (10 - 1) * z

for n in range(p, d + z, z):
    print(f'{n}', end=' -> ')