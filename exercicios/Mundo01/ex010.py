import requests
real = float(input('Quantos reais você tem (Use . ao invés de ,)? '))
opcao = input('Você deseja usar preço online (S=Sim) ? ')
opcao = opcao.upper()
if opcao == 'S' or opcao == '':
    response = requests.get("https://free.currconv.com/api/v7/convert?q=USD_BRL&compact=ultra&apiKey=a44f5ef75d2728680dbc")
    dolar = float(response.json()['USD_BRL'])
else:
    dolar = input('Qual valor do dolar atual?')
print(f'Você com R${real:.2f} (Reais) poderá comprar ${(real/dolar):.2f} (Dolares).')