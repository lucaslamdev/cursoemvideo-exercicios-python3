nome = input('Digite um nome: ').strip()
nomeseparado = nome.split()
print(f'O primeiro nome é {nomeseparado[0]}')
print(f'O último nome é {nomeseparado[(len(nomeseparado)-1)]}')