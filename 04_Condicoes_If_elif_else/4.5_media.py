''' Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''


list_notas = []

qtd_notas = int(input('Digite a quantidade de notas que deseja calcular: '))

while len(list_notas) < qtd_notas:
    r = len(list_notas) + 1
    nota = float(input(f'Digite a {r} nota: '))
    if 0 <= nota <= 10:
        list_notas.append(nota)
    else:
        print('Por favor digite uma nota entre 0 e 10.')

if qtd_notas > 0:
    media = sum(list_notas) / qtd_notas
else:
    media = 0

print(f'O aluno tirou as notas {list_notas}')
print(f'A media sera de {media:.2f} pontos')

if media < 5:
    print('REPROVADO')
elif media < 7:
    print('RECUPERACAO')
else:
    print('APROVADO')