'''Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados.'''

n = int(input("Digite um numero: "))

print(f'O Numero {n} tem ao todo:')

u = n // 1 % 10 #Unidade
d = n // 10 % 10 #Dezenas
c = n // 100 % 10 #Centenas
m = n // 1000 % 10 #Milhas

print(f'Unidades {u}')
print(f'Dezenas {d}')
print(f'Centena {c}')
print(f'Milhar {m}')

