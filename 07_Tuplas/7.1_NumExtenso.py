'''Crie um programa que tenha uma dupla totalmente preenchida
com uma contagem por extenso, de zero até vinte. Seu programa 
deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numeros = (
    "zero","um","dois","três","quatro",
    "cinco","seis","sete","oito","nove","dez",
    "onze","doze","treze","quatorze","quinze",
    "dezesseis","dezessete","dezoito","dezenove","vinte",
)

cont = 0

while cont <= 20:
    num = int(input("Digite o numero que voce deseja: "))
    if num >=0 and num <= 20:
        while cont <= 20:
            print(f'{numeros[cont]}')
            cont += 1
    else:
        print('Por favor digite um numero entre 0 e 20')
        break
    
print('Encerrando o programa')
print(f'O Numero que voce escolheu foi {numeros[num]}')