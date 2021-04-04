# 1 litro = 2m quadrado
print('Vamos pintar uma parede!')
largura = float(input('Qual é a largura da parede em metros? '))
altura = float(input('Qual é a altura da parede em metros? '))
area = largura * altura
print(f'Serão necessarios {area/2:.2f} litros de tinta, para pintar {area:.2f} metros quadrados de parede.')
