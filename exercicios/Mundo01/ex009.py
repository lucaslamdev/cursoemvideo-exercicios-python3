num = int(input('De qual número você quer a tabuada? '))
print(f'A tabuada do {num} é:')
for x in range(11):
    print(f'{num:<2} X {x:<2} = {num*x:<3}')