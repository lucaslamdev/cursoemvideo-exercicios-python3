kmviagem = int(input("Quantos Km foram percorridos durante a viagem? "))
if kmviagem <= 200:
    print(f"Você pagará R$0.50 por km logo será R${(kmviagem*0.50):.2f} pela viagem.")
else:
    print(f"Você pagará R$0.45 por km logo será R${(kmviagem * 0.45):.2f} pela viagem.")