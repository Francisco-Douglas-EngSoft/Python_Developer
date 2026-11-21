#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
pc = randint(0,2)

print('Jogo JOKENPO')
print('*'*30)
print('''
Escolha uma opção para jogar
[0] Pedra
[1] Papel
[2] Tesoura
''')
print('*'*30)

lista = ["Pedra", "Papel", "Tesoura"]


while True:
    op = int(input("Digite sua opção: "))
    if op <= 2:
        print(f'Você Jogou  {lista[op]}')
        print(f'O Computador Jogou {lista[pc]}')
        
        if op == pc:
            print('EMPATE')
            break
        elif op == 0 and pc == 1:
            print("Computador Ganhou")
            break
        elif op == 1 and pc == 2:
            print('Computador Ganhou')
            break
        elif op == 2 and pc == 0:
            print('Computador Ganhou')
            break
            
        elif pc == 0 and op == 1:
            print("Jogador Ganhou")
            break
        elif pc == 1 and op == 2:
            print('Jogador Ganhou')
            break
        elif pc == 2 and op == 0:
            print('Jogador Ganhou')
            break
    else:
        print(f'Por favor digite uma opção valida voce digitou {op}')
    
        
