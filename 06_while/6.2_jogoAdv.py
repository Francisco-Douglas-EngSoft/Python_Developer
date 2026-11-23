'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
em um número entre 0 e 10. Só que agora o jogador vai tentar 
adivinhar até acertar, mostrando no final quantos palpites 
foram necessários para vencer.'''

from random import randint
pc = randint(1, 10)

cont = 0

print('Estou pensando em um numero advinhe qual!')
user = 0

while pc != user:
    user = int(input('Digite um numero: '))
    cont += 1
    if user != pc:
        print(f'Voce errou tente novamente')
        if pc > user:
            print('Digite um Numero Maior')
        else:
            print('Digite um Numero Menor')
            
    elif user == pc:
        print(f'Voce acertou eu pensei em {pc} e voce digitou {user}')
    else:
        print(f'Vamos digita um numero corretamente')

print(f'Voce acertou depois de {cont} tentativas')
