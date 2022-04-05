print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.\nCalcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')

Km = float(input('Quantos km percorridos?: '))
Dias = int(input('Quantos dias foi alugado?: '))

print(f'O preço pelos dias é de R${Dias*60}.')
print(f'O preço pelos km é de R${Km*0.15:.2f}.')
print(f'O preço total a ser pago é de R${(Dias*60)+(Km*0.15):.2f}!')
