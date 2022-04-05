#print('Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.')

'''valores = list()
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'O maior número da lista foi {max(valores)}!')
print(f'O menor número da lista foi {min(valores)}!')
for c, v in enumerate(valores):
    print(f'\nNa posição {c} eu encontrei o valor {v}!', end='')
print('\nFim!')'''

valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-' * 25)
print(f'Os valores digitados foram {valores}!')
print(f'O maior valor digitado foi {maior}! Nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i} / ', end='')
print()
print(f'O menor valor digitado foi {menor}! Nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i} / ', end='')
print()