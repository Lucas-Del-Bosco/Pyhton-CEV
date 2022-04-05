#print('Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:\nconsidere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.')

valor = int(input('Valor a ser sacado: R$'))
total = valor
a = 50
b = 20
c = 10
d = 1
qa = qb = qc = qd = 0
while total != 0:
    if total >= a:
        total -= a
        qa += 1
    elif total >= b:
        total -= b
        qb += 1
    elif total >= c:
        total -= c
        qc += 1
    elif total >= d:
        total -= d
        qd += 1
print(f'{qa} notas de R$50')
print(f'{qb} notas de R$20')
print(f'{qc} notas de R$10')
print(f'{qd} notas de R$1')
