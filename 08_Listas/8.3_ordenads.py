''' Crie um programa onde o usuário possa digitar cinco valores 
numéricos e cadastre-os em uma lista, já na posição correta de 
inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

listaN = []

for n in range(1, 6):
    num = int(input(f'Digite o {n} numero: '))

    if len(listaN) == 0 or num > listaN[-1]:
        listaN.append(num)
    else:
        pos = 0

        while pos < len(listaN):
            if num <= listaN[pos]:
                listaN.insert(pos, num)
                break
            pos += 1

print(f"Os Numeros digitados foram {listaN}")
        