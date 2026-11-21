'''Refaça o DESAFIO 35 dos triângulos, acrescentando 
o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''


lista = []

for r in range(1, 4):
    lado = int(input(f'Digite o {r} lado: '))
    lista.append(lado)

l = lista
print(f'Os Lados do Triangulo são: {lista}')

if l[0] < l[1] + l[2] and lista[1] < l[0] + l[2] and l[2] < l[1] + l[0]:
    print(f'Os Lados Forman um Triangulo do Tipo: ')
    if l[0] == l[1] == l[2]:
        print('EQUILATERO')
    elif l[0] != l[1] != l[2]:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print(f'Os lados não forman um Triangulo')