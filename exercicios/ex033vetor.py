vetor = [int(input("Digite um número: ")) for _ in range(3)]

maior = vetor[0]
menor = vetor[0]

for i in vetor:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f"O maior número é {maior}.")
print(f"O menor número é {menor}.")
