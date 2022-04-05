#print('Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:\nA) qual é o total gasto na compra.\nB) quantos produtos custam mais de R$1000.\nC) qual é o nome do produto mais barato.')

soma = produtos = preçobarato = c = 0
maisbarato = ''
continuar = 'S'
while continuar == 'S':
    produto = str(input('Produto: ')).title()
    preço = float(input('Preço: R$'))
    c += 1
    soma += preço
    if preço > 1000:
        produtos += 1
    if c == 1:
        preçobarato = preço
        maisbarato = produto
    if preçobarato > preço:
        preçobarato = preço
        maisbarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer adicionar mais produtos? [S/N]: ')).upper().strip()[0]
print(f'''O total foi de R${soma:.2f} reais
{produtos} produtos custam mais de R$1000
O produto mais barato é {maisbarato}''')
