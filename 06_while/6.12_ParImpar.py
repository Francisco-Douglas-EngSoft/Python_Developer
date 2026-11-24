'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando 
o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

v = 0
t = 0
cont = 0

while True:
    num = int(input('Digite uma opção para advinha: '))
    op = str(input("Par ou Impar: ")).strip().upper()[0]
    pc = randint(1, 100)
    cont += 1

    if op == "P":
        print(f'Voce escolheu PAR {num}')
        if num % 2 == 0 and pc % 2 == 0:
            print(f"PC Jogou {pc} e voce Jogou {num} Deu EMPATE")
        elif num % 2 == 0 and pc % 2 == 1:
            print(f'PC Jogou {pc} IMPAR e Voce Jogou {num} PAR')
            v += 1
        
    elif op == "I":
        print(f'Voce escolheu PAR {num}')
        if num % 2 == 1 and pc % 2 == 1:
            print(f"PC Jogou {pc} e voce Jogou {num} Deu EMPATE")
        elif num % 2 == 1 and pc % 2 == 0:
            print(f'PC Jogou {pc} PAR e Voce Jogou {num} IMPAR')
            v += 1
    elif op == "S":
        print("Saindo do Programa")
        break
    else:
        print('Digite uma opção valida')

print(f'Ao todo foram jogados {cont} vezes e voce ganhou {v} vezes')
        
    
        
    