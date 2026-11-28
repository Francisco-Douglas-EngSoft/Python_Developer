'''Crie um programa onde o usuário possa digitar vários valores numéricos 
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será 
adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
from time import sleep

listaN = list()
contador = 0

while True:
    num = int(input("Digite um numero: "))
    cont = input("Quer continuar: [S][N] ").upper()
    contador += 1
    
    if cont == "S":
        if num not in listaN:
            listaN.append(num)
        else: 
            pass
    elif cont == "N":
        print('Encerrando o programa........')
        sleep(3)
        break
    else:
        print(f"Digite uma Opção valida [S][N] voce digitou {cont}")
        
print(f'Ao todo foram digitados {contador} numeros')
print(f'Os Numeros Unicos Digitados Foram {listaN}')
print(f'Os Numeros em Ordem são {sorted(listaN)}')