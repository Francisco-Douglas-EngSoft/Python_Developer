'''Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o 
usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

qtd18 = 0
qtdH  = 0
qtdM20 = 0
p = 0

while True:
    nome  = str(input('Digite um nome: '))
    idade = int(input(f'Digite a idade do(a) {nome}: '))
    sexo  = str(input(f'Digite o sexo do(a) {nome} [F][M]: ')).upper()[0]
    p += 1
    cont  = str(input('Quer continuar [S][N]? ')).upper()[0]
    
    if cont == "S":
        if idade >= 18:
            qtd18 += 1
        elif sexo == "F":
            qtdM20 == idade
            if qtdM20 < 20:
                qtdM20 += 1
            else:
                pass
        elif sexo == "M":
            qtdH += 1
    else:
        print('Encerrando')
        break
    
print(f'Ao todo foram digitados um total de {p} Pessoas')
print(f'Foram digitados {qtdH} Homens')
print(f'Foram digitados {qtdM20} Mulheres com menos de 20 anos')
print(f'Ao todo são {qtd18} Pessoas maiores de 18 anos')
        