import os
for x in range(116):
    numarquivo = int(x)
    str(numarquivo)
    if numarquivo <= 9 and numarquivo >=0:
        arquivo = str(f'ex00{numarquivo}.py')
    if numarquivo <= 99 and numarquivo > 10:
        arquivo = str(f'ex0{numarquivo}.py')
    if numarquivo <= 115 and numarquivo > 100:
        arquivo = str(f'ex{numarquivo}.py')
    if not os.path.exists(arquivo):
        open(arquivo, 'w').close()
        print(f'File {arquivo}, created!')
    else:
        print(f'File {arquivo}, not created!')