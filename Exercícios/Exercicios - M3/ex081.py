#print('Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:\nA) Quantos números foram digitados.\nB) A lista de valores, ordenada de forma decrescente.\nC) Se o valor 5 foi digitado e está ou não na lista.')

lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]: ')).strip()[0]
    cont += 1
    if resposta in 'Nn':
        break
lista.sort(reverse=True)
print(f'Você digitou {cont} números!\nOs valores em ordem descrescente são {lista}')
print(f'O valor 5 faz parte da lista!' if 5 in lista else 'O valor 5 não faz parte da lista!')
