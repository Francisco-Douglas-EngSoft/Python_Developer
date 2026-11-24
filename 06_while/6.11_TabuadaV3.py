'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.'''

while True:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Calcula ate o numero: "))
    
    print('-'*20)
    print('''
    Opção para Calculo:
    [1] Soma
    [2] Subtração
    [3] Divisão
    [4] Multiplicação
    [5] Sair''')
    print('-'*20)
    
    op = int(input('Digite uma opção: '))
    if op == 1:
        print(f'Soma')
        for n in range(1, n2):
            print(f'{n1} + {n2} = {n1+n2}')
    elif op == 2:
            print(f'Subtração')
            for n in range(1, n2):
                print(f'{n1} - {n2} = {n1-n2}')
    elif op == 3:
            print(f'Divisão')
            for n in range(1, n2):
                print(f'{n1} / {n2} = {n1/n2}')
    elif op == 4:
            print(f'Multiplicação')
            for n in range(1, n2):
                print(f'{n1} * {n2} = {n1*n2}')
    elif op <= 0 or op == 5:
        print(f'Sair do Programa')
        break
    else:
        print('Por favor digite uma opção valida')