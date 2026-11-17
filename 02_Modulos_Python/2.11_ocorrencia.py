"""Faça um programa que leia uma frase pelo teclado 
e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e 
em que posição ela aparece a última vez."""

palavra = str(input("Digite a Palavra: ")).upper()

print(f'A Letra A Apareceu a primeira vez na Posição {palavra.find("A")+1}')
print(f'A Letra A Apareceu a ultima vez na Posição {palavra.rfind("A")+1}')
print(f'Ao todo apareceu {palavra.count("A")} vezes')