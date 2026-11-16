'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

numero = int(input("Digite um numero: "))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print(f'O Numero digitado foi {numero}')
print(f'O Dobro de {numero} e {dobro}')
print(f'O Triplo de {numero} e {triplo}')
print(f'A Raiz Quadrada de {numero} e {raiz:.2f}')