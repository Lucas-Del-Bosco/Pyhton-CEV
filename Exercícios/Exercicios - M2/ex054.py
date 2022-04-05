print('Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.')

from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}ª pesssoa: '))
    idade = atual - ano
    if idade >= 18:
        maiores += 1
    elif idade < 18:
        menores += 1
print(f'A quantidade de pessoas que são maiores de idade é {maiores}!')
print(f'A quantidade de pessoas que são menores de idade é {menores}!')
