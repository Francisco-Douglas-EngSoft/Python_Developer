''' Escreva um programa em Python que leia um número inteiro qualquer e peça para 
o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''


numero = int(input('Digite o numero para Conversão: '))

print(f'O Numero digitado foi {numero} convertidos para')

print('*'*30)
print('''
      Digite uma opçao para conversão
      [1] Binario
      [2] Octal
      [3] Hexadecimal
      ''')
print('*'*30)

opcao = int(input(f'Digite uma opção para converter o numero {numero}: '))

if opcao == 1:
    print(f'Binario: {bin(numero)}')
elif opcao == 2:
    print(f'Octal: {oct(numero)}')
elif opcao == 3:
    print(f'Hexadecimal: {hex(numero)}')
else:
    print(f'Por favor digite uma opção valida voce digitou {opcao}')