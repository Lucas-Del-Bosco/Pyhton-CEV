#print('Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.')

lista = []
resposta = 'S'
while resposta == 'S':
    valor = (int(input('Digite um valor: ')))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor repetido, não adicionado!')
    resposta = str(input('Quer adicionar outro número? [S/N]: ')).upper().strip()[0]
lista.sort()
print(f'Você digitou os números: {lista}!')
