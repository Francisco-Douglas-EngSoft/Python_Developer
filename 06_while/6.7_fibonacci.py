'''Escreva um programa que leia um número N inteiro qualquer e mostre 
na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:'''

qtd = int(input('Quantos termos deseja mostra: '))
f0 = 0
f1 = 1
contador = 0

while contador < qtd:
    print(f0, end="-> ")
    f0, f1 = f1, f0 + f1
    contador += 1
    
print('Programa encerrado:')
    