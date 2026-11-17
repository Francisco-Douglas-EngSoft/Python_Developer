#Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome da Cidade: '))
cit = cidade.strip()

print(f'O Nome começa com SANTO em Maiusculo: {"SANTO" in cit[:5]}')
print(f'O Nome começa com Santo: {"Santo" in cit[:5]}')
