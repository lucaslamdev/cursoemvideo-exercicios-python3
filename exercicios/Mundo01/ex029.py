velocidade = float(input("Digite a velocidade em que você está: "))

if velocidade > 80:
    kmacima = float(velocidade-80)
    print(f"Por estar acima da velocidade permitida de 80Km voce foi multado em R${(kmacima*7.0):.2f} ")
    print("Sendo R$7.00 a cada km acima do limite.")
else:
    print("Parabéns você é um Motorista exemplar e não ultrapassou 80Km por hora!")