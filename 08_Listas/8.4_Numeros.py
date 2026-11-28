'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

listaN = []

while True:
    numeros = int(input('Digite um numero: '))
    continua = input("Quer continuar [S][N]: ").upper()
    
    listaN.append(numeros)
    if continua == "S":
        pass
    else:
        print("Encerrando o programa")
        break
    
print(f'Ao todo foram digitados {len(listaN)} numeros')
print(f'A ordem digitada foi {listaN}')
listaN.sort()
print(f'OS numeros em Ordem {listaN}')
listaN.sort(reverse=True)
print(f'Os numeros em Ordem Decrescente {listaN}')
if 5 in listaN:
    print(f'O Valor 5 foi digitado na posição {listaN.index(5)}')
else:
    print('O Valor 5 não foi digitado')