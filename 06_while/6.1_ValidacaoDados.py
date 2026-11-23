'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os 
valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação 
novamente até ter um valor correto.'''

while True:
    sexo = str(input('Digite o sexo ou [S] para sair [M][F]')).title()
    if sexo == "S":
        print('Saindo do Programa')
        break
    elif sexo == "M":
        print(f'O Sexo digitado foi {sexo} Masculino')
    elif sexo == "F":
        print(f'O Sexo digitado foi {sexo} Feminino')
    else:
        print(f'Por favor digite um sexo valido voce digitou {sexo}')
