print('Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.')

print('==' * 20)
print('         PROGRESSÃO ARITMÉTICA')
print('==' * 20)
t1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da progessão: '))
décimo = t1 + (10 - 1) * r
for c in range(t1, décimo + r, r):
    print(c, end=' -> ')
print('FIM')
