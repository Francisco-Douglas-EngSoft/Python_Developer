'''Faça um programa que leia o comprimento do cateto oposto e do cateto 
adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.'''

from math import hypot

cateto_oposto = int(input("Digite o Cateto Oposto: "))
cateto_adjacente = int(input("Digite o Cateto Adjacente: "))

hipot_mod = hypot(cateto_adjacente, cateto_adjacente)

print(f"O Valor da Hipotenuza sera de {hipot_mod}")