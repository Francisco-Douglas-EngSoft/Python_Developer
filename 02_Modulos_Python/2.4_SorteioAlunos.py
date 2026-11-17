'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, 
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

from random import choice

lista = []

for nome in range(1, 5):
    nomes = input(f'Digite o nome do {nome} aluno: ')
    lista.append(nomes)

print(f"A Lista de Alunos e {lista}")
escolhido = choice(lista)
print(f"O Aluno escolhido foi {escolhido}")