#print('Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.')

while True:
    num = int(input('Digite um número para ver a tabuada: '))
    print('-' * 40)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 40)
    if num < 0:
        break
print('Programa encerrado!')
