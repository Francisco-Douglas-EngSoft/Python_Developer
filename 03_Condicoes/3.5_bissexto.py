'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

from datetime import date
atual = date.today().year
print(atual)

ano = int(input("Digite um ano para analisar: "))


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o Ano {ano} e Bissexto')
else:
    print(f'O Ano {ano} não e Bissexto')