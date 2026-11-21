'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''

produto = input('Nome do Produto: ')
valor = float(input(f'Valor do {produto} R$: '))

print(f'O Produto a Ser comprado é {produto} com o valor atual de {valor}R$')

print('-'*25)
print('''
Formas de Pagamento
[1] A vista dinheiro/cheque 10% de desconto
[2] A vista cartão de credito 5% de desconto
[3] Em ate 2x no cartao preço formal
[4] 3x ou mais 20% de juros''')

pg = int(input('Digite a sua forma de pagamento: '))

if pg == 1:
    print('Pagamento A Vista')
    nvalor = valor - (valor * 0.1)
    print(f'O Preço com desconto de 10% sera de {nvalor:.2f}R$')
elif pg == 2:
    print('A Vista no cartão:')
    nvalor = valor - (valor * 0.05)
    print(f'O Preço com desconto de 5% sera de {nvalor:.2f}R$')
elif pg == 3:
    print('Em ate 2X no cartao Preço Normal sem Desconto')
elif pg == 4:
    print('3X Juros de 20%')
    nvalor = valor + (valor * 0.2)
    parc = int(input('Digite o total de parcelas: '))
    vparc = nvalor / parc
    print(f'O Novo valor com Juros sera de {nvalor:.2f}R$ e serão {parc} parcelas serao de {vparc:.2f}R$')
else:
    print(f'Por favor digite uma opção valida voce digitou {pg}')