'''Faça um programa que calcule a soma entre todos os números que 
são múltiplos de três e que se encontram no intervalo de 1 até 500.'''


cont = 0
soma = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1
        soma += n
    else:
        pass
    
print(f'De 1 a 500 temos {cont} numeros multiplos de 3 e a soma total e {soma}')