from math import sin,cos,tan,radians
angulo = float(input('Digite um ângulo: '))
radiano = radians(angulo)
print(f'Seu seno é {sin(radiano):.2f}.')
print(f'Seu cosseno é {cos(radiano):.2f}.')
print(f'Seu tangente é {tan(radiano):.2f}.')