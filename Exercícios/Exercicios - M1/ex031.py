print('Desenvolva um programa que pergunte a distância de uma viagem em Km.\nCalcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.')

d = float(input('Qual a distância da viagem?: '))
if d <= 200:
    print(f'O custo da passagem é de R${d*0.50:.2f}')
else:
    print(f'O custo da passagem é de R${d*0.45:.2f}')

d = float(input('Qual a distância da viagem?: '))
preço = d * 0.50 if d <= 200 else d * 0.45
print(f'O preço da sua viagem é de R${preço}')
