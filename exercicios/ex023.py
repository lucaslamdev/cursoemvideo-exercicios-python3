num = input('Digite um número de 0 a 9999: ')
if 0 <= int(num) <= 9999:
    if len(num) >= 1:
        print(f'Unidade: {num[len(num)-1]}.')
    if len(num) >= 2:
        print(f'Dezena: {num[(len(num)-2)]}.')
    if len(num) >= 3:
        print(f'Centena: {num[(len(num)-3)]}.')
    if len(num) == 4:
        print(f'Milhar: {num[(len(num)-len(num))]}.')
else:
    print(f'Valor informado ({num}) fora dos valores entre 0 a 9999')
