print('Faça um programa que leia um número qualquer e mostre o seu fatorial.')

'''from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}!')'''#Fatorial Python

'''n = int(input('Digite um número: '))
c = n
f = 1
print(f'O valor de {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
    c -= 1
print(f'{f}.')'''#Fatorial While

'''n = int(input('Digite um número: '))
f = 1
for valor in range(n, 0, -1):
    print(f'{valor}', end='')
    if valor > 1:
        print(' x ', end='')
    else:
       print(' = ', end='')
    f *= valor
print(f)'''#Fatorial For
