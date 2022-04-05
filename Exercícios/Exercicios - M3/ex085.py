#print('Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.')

'''números = []
for c in range(1, 8):
    números.append(int(input(f'Digite o {c}º valor: ')))
print(f'Os números pares são: ', end='')
for c in números:
    if c % 2 == 0:
        print(f'{sorted({c})} ', end='')
print()
print(f'Os números ímpares são: ', end='')
for c in números:
    if c % 2 == 1:
        print(f'{sorted({c})} ', end='')'''

números = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        números[0].append(valor)
    else:
        números[1].append(valor)
números[1].sort()
números[0].sort()
print('=-' * 30)
print(f'Os valores ímpares são {números[1]}')
print(f'Os valores pares são {números[0]}')

