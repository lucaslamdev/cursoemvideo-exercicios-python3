dias = int(input('Por quantos dias você alugou o carro? '))
kmrodados = float(input('Quantos km você rodou? '))
print(f'Você terá que pagar R${float((dias*60)+(kmrodados*0.15)):.2f} .')
print(f'Pelo(s) {dias} dia(s) alugado(s) e pelo(s) {kmrodados:.2f} km(s) rodados.')
