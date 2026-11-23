'''Melhore o DESAFIO 61, perguntando para
o usuário quantos termos ele quer mostrar a mais.
O programa encerrará quando ele informar 0 termos.'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = primeiro
total = 10

cont = 1
while cont <= total:
    print(f'{termo}', end=' -> ' if cont < total else '\n')
    termo += razao
    cont += 1

while True:
    quantidade = int(input('Quantos termos você quer mostrar a mais? '))

    if quantidade == 0:
        break

    if quantidade < 0:
        print('Digite uma quantidade igual ou maior que zero.')
        continue

    cont = 1
    while cont <= quantidade:
        print(f'{termo}', end=' -> ' if cont < quantidade else '\n')
        termo += razao
        cont += 1