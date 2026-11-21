#Tabuada

num = int(input('Digite um numero para calcular: '))
print('-'*10)
print('[+] [-] [*] [/]')
print('-'*10)

op = str(input('Digite uma opção: ')).upper()

for n in range(1, 11):
    if op == "+":
        print(f'{num} + {n} = {num+n} ')
    elif op == "-":
        print(f'{num} - {n} = {num-n} ')
    elif op == "*":
        print(f'{num} x {n} = {num*n} ')
    elif op == "/":
        print(f'{num} / {n} = {num/n} ')
    else:
        print('Digite uma opção valida')
print('Encerrando Programa')