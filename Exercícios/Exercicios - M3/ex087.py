#print('Aprimore o desafio anterior, mostrando no final:\nA) A soma de todos os valores pares digitados.\nB) A soma dos valores da terceira coluna.\nC) O maior valor da segunda linha.')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {[l, c]}: '))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {spar}!')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}!')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segunda linha é {maior}!')