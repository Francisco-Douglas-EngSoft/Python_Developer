'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

print(f'Os Numeros digitados foram {n1} - {n3} - {n3}')
if n1 and n2 and n3 > 0:
    if n1 > n2 > n3:
        print(f'O Numero {n1} é Maior')
    elif n2 > n1 > n3:
        print(f'O Numero {n2} é Maior')
    else:
        print(f'O Numero {n3} é Maior')
if n1 and n2 and n3 > 0:
    if n1 < n2 < n3:
        print(f'O Numero {n1} e Menor')
    elif n2 < n1 < n3:
        print(f'O Numero {n2} e Menor')
    else:
        print(f'O Numero {n3} e Menor')
else:
    print('Digite um valor maior que 0')