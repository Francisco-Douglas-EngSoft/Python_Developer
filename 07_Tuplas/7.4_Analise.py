'''Desenvolva um programa que leia quatro valores pelo 
teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

lista = []
cont9 = 0
par = []

for v in range(1, 5):
    n = int(input(f"Digite o {v} numero: ")),
    lista.append(n)
        
tupla = lista
print(f'O Valor 9 Apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O Numero 3 Apareceu na posicao {tupla.index(3)}')
else:
    print('O Valor 3 não foi digitado')

for n in tupla:
    if n % 2 == 0:
        print(f'Os Numeros pares Digitados foram {n}')