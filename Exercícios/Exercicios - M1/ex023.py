print('Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.')

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}: ')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')


num = str(input('Digite um número de 0 a 9999: ')).zfill(4)
print(f'O número digitado foi {num}')
print(f'Unidade: {num[3]}\nDezena: {num[2]}\nCentena: {num[1]}\nMilhar: {num[0]}')
