retas = [int(input("Digite o tamanho de uma reta em cm: ")) for _ in range(3)]
if retas[0] < (retas[1] + retas[2]) and retas[1] < (retas[0] + retas[2]) and retas[2] < (retas[0] + retas[1]):
    print("É possível formar um triângulo.")
else:
    print("Não é possível formar um triângulo.")
