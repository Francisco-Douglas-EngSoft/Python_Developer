'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
from datetime import date
hoje = date.today().year

pessoas = []
maiorIdade  = []

for n in range(1, 8):
    p = str(input(f'Nome da {n} pessoa: '))
    i = int(input(f'Data de Nascimento da {p}: '))
    pessoas.append(p)
    idade = hoje - i
    if idade >= 18:
        maiorIdade.append(p)
    else:
        pass
print(f'Nomes das Pessoas Digitadas {pessoas}')
print(f'Das 7 pessoas apenas {maiorIdade} são Maiores de Idade')
    
    