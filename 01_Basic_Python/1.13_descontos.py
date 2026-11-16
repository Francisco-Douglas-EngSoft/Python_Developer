'''Faça um algoritmo que leia o preço de 
um produto e mostre seu novo preço, com 5% de desconto.'''

produto = str(input("Digite o nome do produto: "))
preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (em %): "))
novo_preco = preco - (preco * desconto / 100)
print(f'O produto {produto} com desconto de {desconto}% tem o novo preço de R$ {novo_preco:.2f}.')