print('hello wold')

valor = int(input(f'Qual tabuada que saber ?'))

v = None
print(f'Tabuada Do {valor}')
      
for v in range(1,11):
    print(f'{v} X {valor} = {v*valor}')

if v:
    print('True')
else:
    print('fals')


lis = []

for v in range(0,11):
    lis.append(v)
print(lis)