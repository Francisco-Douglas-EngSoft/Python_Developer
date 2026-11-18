#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input("Digite um numero: "))

if n > 0:
    if n % 2 == 0:
        print(f"O Numero {n} é PAR")
    else:
        print(f'O Numero {n} é IMPAR')
        
else:
    print(f'O Numero deve ser maior que 0 voce digitou {n}')