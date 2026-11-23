'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

media = 0
soma  = 0
total = 0

while True:
    num = int(input('Digite um Numero: '))
    mais = input('Quer continuar [S][N]: ').upper()
    soma += num
    total += 1
    
    if mais == "S":
        continue
    elif mais == "N":
        break
    else:
        print(f'Digite um opcao valida voce digitou {mais}')
        
media = soma / total
print(f'Ao todo foram digitados {total} numeros')
print(f'A Soma dos {total} numeros e {soma}')
print(f'A Media final e de {media}')