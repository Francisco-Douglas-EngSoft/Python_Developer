'''Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

nome = str(input("Digite o seu nome: ")).capitalize()
print(f'Nome com Todas as Letras Maiusculas: {nome.upper()}')
print(f'Nome com Todas as Letras Minusculas: {nome.lower()}')
print(f'Total de Letras sem Espaços {len(nome) - nome.count(' ')}')
print(f'Total de letras o Primeiro nome {nome.find(' ')}')