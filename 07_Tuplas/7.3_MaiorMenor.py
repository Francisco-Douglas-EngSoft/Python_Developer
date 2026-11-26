''' Crie um programa que vai gerar cinco números aleatórios e colocar 
em uma tupla. Depois disso, mostre a listagem de números gerados e 
também indique o menor e o maior valor que estão na tupla.'''

from random import randint as rand

numeros = ((rand(1,10), rand(1,10), rand(1,10), rand(1,10), rand(1,10)))

print(f'Lista de Numeros Gerados {numeros}')
print(f'O Maior Numero e {max(numeros)}')
print(f'O Menor Numero e {min(numeros)}')