'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
em um número entre 0 e 10. Só que agora o jogador vai tentar 
adivinhar até acertar, mostrando no final quantos palpites 
foram necessários para vencer.'''

from random import randint
pc = randint(1, 10)

cont = 0

print('Estou pensando em um numero advinhe qual!')

