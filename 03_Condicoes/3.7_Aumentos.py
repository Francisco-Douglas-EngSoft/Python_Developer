'''Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a 
R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%.'''

func = str(input("Digite o nome do Funcionario: ")).title()
sal = float(input(f"Digite o Salario do {func}: R$ "))

print(f'O Funcionario {func} que ganhava {sal}R$ de Salario Mensal.')

if sal > 0:
    if sal >= 1250:
        novoS = sal + (sal * (10 / 100))
        print(f'Terá um aumento de 10% seu novo Salario sera de {novoS}R$')
    else:
        novoS = sal + (sal * (10 / 100))
        print(f'Terá um aumento de 15% seu novo Salario sera de {novoS}R$')
        
else:
    print('Digite um Salario Acima de 0')