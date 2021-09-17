catetoOposto = float(input('Qual é o comprimento do cateto oposto em cm? '))
catetoAdjacente = float(input('Qual é o comprimento do cateto adjacente em cm? '))
hipotenusa = ((catetoOposto**2)+(catetoAdjacente**2))**(1/2)
print(f'O comprimento da hipotenusa é de {hipotenusa:.2f}cm.')
