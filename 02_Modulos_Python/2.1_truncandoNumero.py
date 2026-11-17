# Crie um programa que leia um número Real qualquer pelo 
# teclado e mostre na tela a sua porção Inteira.

from math import trunc

numero = 345.674

print(f'Número com uma casa decimal: {numero:.0f}')
print(f'Numero convertido {int(numero)}')
print(f'Número truncado: {trunc(numero)}')