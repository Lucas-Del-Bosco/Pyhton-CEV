print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada: ')

n = float(input('Escolha um número inteiro: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'De acordo com o número escolhido {n:.2f}, podemos afirmar:\nDobro: {d:.2f}\nTriplo: {t:.2f}\nRaiz Quadrada: {r:.2f}')
