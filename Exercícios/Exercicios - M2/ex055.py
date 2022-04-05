print('Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos')

maior = 0
menor = 0
for grupo in range(1, 6):
    peso = float(input(f'Peso da {grupo}ª pessoa: '))
    if grupo == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso é {maior}kg')
print(f'O menor peso é {menor}kg')

