'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

custo = 0
total = 0
menor = 0
maior = 0
barato = ''

while True:
    produto = input('Digite o produto: ').upper()
    preco   = float(input(f'Digite o preco do {produto}: '))
    op  = str(input('Quer continua: [S][N]. ')).upper()[0]
    custo += preco
    total += 1
    
    
    if op == "S":
        if preco >= 1000:
            maior += 1
        elif total == 1:
            menor = preco
            barato = produto
        else:
            if preco < menor:
                menor = preco
                barato = produto
    else:
        print('Saindo do Programa')
        break
    
print(f'Ao todo foram comprados {total} Produtos')
print(f'O Custo total da compra foi de {custo:.2f} R$')
print(f'O Menor produto e {produto} com o preco de {menor:.2f} R$')
print(f'Ao todo temos {maior} produtos que custam mais de 1000')
        