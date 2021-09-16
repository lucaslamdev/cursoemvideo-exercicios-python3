salario = float(input("Qual é seu salário? "))

if salario > 1250:
    print(f"Você terá um aumento e 10%, logo seu salário passara a ser de R${(salario+(salario*0.10)):.2f}")
else:
    print(f"Você terá um aumento e 15%, logo seu salário passara a ser de R${(salario+(salario*0.15)):.2f}")