'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente. Ao final, 
mostre o conteúdo das três listas geradas.'''

listaN = [] 
par = [] 
impar = []

while True:
    numeros = int(input("Digite o numero: "))
    resp = str(input("Quer continuar [S][N]: ")).upper()
   
    if resp != 'N':
        listaN.append(numeros)     
    else:
        print('Encerrando o programa')
        break
for indice, valor in enumerate(listaN):
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 == 1:
        impar.append(valor)
print(f'Ao todo foram digitados {len(listaN)}')
print(f'Os Numeros PARES digitados foram {par}')
print(f'Os Numeros IMPARES digitados foram {impar}')