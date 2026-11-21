'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

peso = float(input(f'Digite o peso do usuario: '))
altura = float(input(f'Digite a Altura do usuario: '))

imc = peso / (altura * altura)

print(f'O Usuario que tem {peso}Kg e um altura de {altura} Metros tera um IMC de: ')

if imc < 18.5:
    print(f'{imc} Abaixo do Peso')
elif imc > 18.5 and imc < 25:
    print(f'{imc} Peso Ideal')
elif imc > 25 and imc < 30:
    print(f'{imc} Sobrepeso')
elif imc > 30 and imc < 40:
    print(f'{imc} Obesidade')
else:
    print(f'{imc} Obesidade Morbida')