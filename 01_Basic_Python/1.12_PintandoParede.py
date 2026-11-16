'''Faça um programa que leia a largura e a altura de 
uma parede em metros, calcule a sua área e a quantidade 
de tinta necessária para pintá-la, sabendo que cada
litro de tinta pinta uma área de 2 metros quadrados.'''

altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))
area = altura * largura
litros_tinta = area / 2

print('A área da parede é de {:.2f} metros quadrados.'.format(area))
print('A quantidade de tinta necessária é de {:.2f} litros.'.format(litros_tinta))