cidade = input('Digite o nome de uma cidade:')
cidade = cidade.split()
if 'SANTO' in cidade[0].upper():
    print('A palavra SANTO é o primeiro nome da cidade!')
else:
    print('Não exite a palavra \'SANTO\' no primeiro nome da cidade')
