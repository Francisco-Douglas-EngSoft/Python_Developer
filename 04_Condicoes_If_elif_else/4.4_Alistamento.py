'''Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date

atual = date.today().year


nome = str(input("Nome do usuario: "))
dtNasc = int(input(f'Data de Nascimento do {nome}: '))

idade = atual - dtNasc
print(f'O Usuario que nasceu em {dtNasc} hoje tem {idade} anos de idade')

if idade >= 18:
    passou = idade - 18
    print(f'Ja era para esta alistado pois passou {passou} do Alistamento')
    
elif idade < 18:
    print(f'Aind não ira se alista no Serviço milita pois so tem {idade}')
    falta = 18 - idade
    print(f'Ainda faltam {falta} para se alista')
else:
    print(f'Por favor digite uma data valida voce digitou {dtNasc}')