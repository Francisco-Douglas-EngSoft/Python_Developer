"""Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e todas as informações possíveis sobre ele.
"""

a = input("Digite algo: ")

print(f'O tipo primitivo e {type(a)}')
print(f'SO tem espaços {a.isspace()}')
print(f'Esta em maiusculas {a.isupper()}')
print(f'Esta em minusculas {a.islower()}')
print(f'E um numero {a.isnumeric()}')
print(f'E Alfabetico {a.isalpha()}')