'''A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e mostre sua 
categoria, de acordo com a idade:

– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''


from datetime import date
atual = date.today().year

ano_nasc = int(input(f'Digite o ano de Nascimento: '))
idade = atual - ano_nasc

print(f'O Joven que nasceu em {ano_nasc} hoje ano atual tem {idade} anos')

if idade <= 9:
    print(f'Classificação MIRIN')
elif idade <= 14:
    print(f'Classificação INFANTIL')
elif idade <= 19:
    print(f'Classificação JUNIOR')
elif idade <= 25:
    print(f'Classificação SENIOR')
else:
    print(f'Classificação MASTER')