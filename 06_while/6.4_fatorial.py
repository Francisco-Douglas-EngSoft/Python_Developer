'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''


n = int(input('Digite um numero para o fatorial: '))
cont = n
tot = 1
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    tot *= cont
    cont -= 1
    
print(f'O Resultado final do Fatorial e {tot}')