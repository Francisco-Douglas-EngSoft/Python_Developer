'''Desenvolva um programa que leia seis números inteiros e mostre 
a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.'''

cont = 0
soma = 0
for n in range(1, 7):
    num = int(input(f'Digite o {n} numero: '))
    if num % 2 == 0:
        cont += 1
        soma += num
        print(f'O Numero {num} é Par')
    else:
        pass
print(f'Foram digitados {cont} numeros pares e a soma e de {soma}')