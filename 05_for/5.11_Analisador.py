'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o 
nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''


soma_idade = 0
maior_idade_homem = 0
mais_velho = ''
mulher20 = 0

for n in range(1, 5):
    print(f'----- {n}ª PESSOA -----')
    nome = input(f'Nome da {n}ª pessoa: ').strip()
    idade = int(input(f'Idade de {nome}: '))
    sexo = input(f'Sexo de {nome} [M/F]: ').strip().upper()
    
    # 1. Acumula as idades para calcular a média depois
    soma_idade += idade
    
    # 2. Verifica se é homem e se tem a maior idade até agora
    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            mais_velho = nome
            
    # 3. Verifica se é mulher e tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulher20 += 1

media_idade = soma_idade / 4

print(f'\nA média de idade do grupo é de {media_idade:.1f} anos.')
if mais_velho != '':
    print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {mais_velho}.')
else:
    print('Não foi cadastrado nenhum homem no grupo.')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos.')