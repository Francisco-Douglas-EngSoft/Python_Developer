'''Escreva um programa que leia dois números inteiros e compare-os. 
mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''
listN = []

for n in range(1, 4):
    numero = int(input(f'Digite o {n} Numero: '))
    listN.append(numero)
print(f'Os Numeros Digitados Foram {listN}')

if listN[0] > listN[1] and listN[0]> listN[2]:
    print(f'O Numero {listN[0]} é maior')
    if listN[1] > listN[2]:
        print(f'O Numero {listN[2]} e o Menor')
    else:
        print(f'O Numero {listN[1]} e o Menor')
elif listN[1] > listN[0] and listN[1] > listN[2]:
    print(f'O Numero {listN[1]} é o Maior')
    if listN[0] > listN[2]:
        print(f'O Numero {listN[0]} e o Menor')
    else:
        print(f'O Numero {listN[2]} e o Menor')
elif listN[0] == listN[1] == listN[2]:
    print('Os Numeros são todos iguais')
else:
    print(f'O Numero {listN[2]} e o Maior')
    if listN[0] > listN[1]:
        print(f'O Numero {listN[0]} e o Menor')
    else:
        print(f'O Numero {listN[1]} e o Menor')