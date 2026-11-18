"""Faça um programa que leia o nome completo de uma 
pessoa, mostrando em seguida o primeiro e o último nome separadamente."""

nome = str(input("Digite o nome completo: ")).strip().title()
nome = nome.split()
print(f'Seu Nome completo e {nome}')

print(f'Seu Primeiro Nome é {nome[0]}')
print(f'Seu Ultimo Nome é {nome[-1]}')