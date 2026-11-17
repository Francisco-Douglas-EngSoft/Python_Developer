'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

pessoa = str(input('Digite o nome da pessoa: ')).upper()

print(f'Existe SILVA no nome {"SILVA" in pessoa}')