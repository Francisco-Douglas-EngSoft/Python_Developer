'''Faça um programa que leia um ângulo qualquer e mostre 
na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import sin, cos, tan

angulo = float(input("Digite o valor do Angulo: "))

seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print(f'O Angulo de {angulo} terá:')
print(f'Seno de {seno}')
print(f'Cosseno de {cosseno}')
print(f'Tangente de {tangente}')