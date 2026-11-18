'''Escreva um programa que faça o computador “pensar” em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual 
foi o número escolhido pelo computador. O programa deverá escrever
na tela se o usuário venceu ou perdeu.'''

from random import randint

n = randint(0,10)

print('Advinhe o Numero que estou pensando? ')

numero = int(input("Digite o numero que voce acha: "))
if numero == n:
    print(f"Parabens Voce acertou eu pensei em {n} e voce chutou {numero}")
    
else:
    print(f'Voce errou eu pensei em {n} e voce chutou {numero}')