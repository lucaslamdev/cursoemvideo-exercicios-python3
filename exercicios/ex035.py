reta1 = int(input("Digite o tamanho de uma reta em cm: "))
reta2 = int(input("Digite o tamanho de uma reta em cm: "))
reta3 = int(input("Digite o tamanho de uma reta em cm: "))
if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print("É possível formar um triângulo.")
else:
    print("Não é possível formar um triângulo.")