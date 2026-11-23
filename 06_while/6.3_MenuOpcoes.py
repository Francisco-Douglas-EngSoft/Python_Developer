'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa'''



opcao = 0

while opcao != 6:
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    print('='*30)
    menu = ('''
        Escolha uma Opção de Calculo
        [1] Somar
        [2] Multiplicar
        [3] Dividir
        [4] SubTrair
        [5] Novos Numeros
        [6] Sair do Programa
        ''')
    print(menu)
    print('='*30)
    op = int(input('Digite uma opcao para calculo: '))
    
    
    if op == 1:
        print(f'Soma {n1} + {n2} = {n1+n2}')
    elif op == 2:
            print(f'Multiplicar {n1} x {n2} = {n1*n2}')
    elif op == 3:
            print(f'Dividir {n1} / {n2} = {n1/n2}')
    elif op == 4:
            print(f'Subtrair {n1} - {n2} = {n1-n2}')
    elif op == 5:
            print(f'Novos Numeros')
            n1 = int(input('Digite o primeiro numero: '))
            n2 = int(input('Digite o segundo numero: '))
    elif op == 6:
            print('Saindo do Programa')
            break
    else:
        print('Digite uma Opção valida')
    
    