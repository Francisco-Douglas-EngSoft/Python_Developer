'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de 
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos 
e mostre a ordem sorteada.'''

from random import shuffle

alunos = []

for n in range(1, 5):
    nomes = str(input(f'Digite o nome do {n} aluno: '))
    alunos.append(nomes)

print(f'A Lista real dos Alunos e: {alunos}')
shuffle(alunos)
print(f'A Ordem Sorteada foi {alunos}')