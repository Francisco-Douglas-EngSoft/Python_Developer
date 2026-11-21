"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o 
salário do comprador e em 
quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""


nome = str(input('Nome do Comprador: ')).title()
salario = float(input(f'Salario mensal do {nome}: R$ '))

valor_imovel = float(input('Valor do Emprestimo para compra do Imovel: R$ '))
meses = int(input('Tempo em meses do Financiamento: '))

tot_anos = meses / 12
max_sal = salario * 0.3
valor_parcelas = valor_imovel / meses

print(f'O Senhor(a) {nome} tem um salario mensal de {salario:.2f}R$')
print(f'Ele pretende financia uma casa de {valor_imovel:.2f}R$ em {tot_anos} Anos')


if meses >= 60:
    juros = 1.5 # 1.5% ao mes
    v_parcela = valor_parcelas + (valor_parcelas * (2 /100))
    print(f'O Valor das Parcelas ficaram em {v_parcela:.2f}R$ por mes com o total de {meses} a uma taxa de {juros}%')
    if v_parcela > max_sal:
        print(f'O Emprestimo sera negado pois o Valor das Parcelas que e de {v_parcela:.2f}R$ excede os 30% de {max_sal:.2f}')
    else:
        print(f'O Emprestimo sera concedido: Valor das Parcelas {v_parcela:.2f}R$ Limite de 30% {max_sal:.2f}R$')
else:
    juros = 2 # 2% ao mes de Juros
    v_parcela = valor_parcelas + (valor_parcelas * (2 /100))
    print(f'O Valor das Parcelas ficaram em {v_parcela:.2f}R$ por mes com o total de {meses} a uma taxa de {juros}%')
    if v_parcela > max_sal:
        print(f'O Emprestimo sera negado pois o Valor das Parcelas que e de {v_parcela:.2f}R$ excede os 30% de {max_sal:.2f}')
    else:
        print(f'O Emprestimo sera concedido: Valor das Parcelas {v_parcela:.2f}R$ Limite de 30% {max_sal:.2f}R$')
    