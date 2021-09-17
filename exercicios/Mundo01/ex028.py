from random import randint

numeroPensando = randint(0,5)
print("O computador pensou um número entre 0 e 5 tente adivinhar!")
numeroDigitado = int(input('Que número você acha q eu pensei? '))
if numeroDigitado == numeroPensando:
    print('Parabéns você acertou!')
else:
    print(f'Que triste você perdeu, o número era {numeroPensando}.')