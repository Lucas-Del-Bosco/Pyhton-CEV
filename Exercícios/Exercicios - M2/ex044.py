print('Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:\n– à vista dinheiro/cheque: 10% de desconto\nà vista no cartão: 5% de desconto\nem até 2x no cartão: preço formal \n3x ou mais no cartão: 20% de juros')

preço = float(input('Valor do produto: R$'))
print(f'Para o pagamento de R${preço} disponibilizamos as formas a seguir:')
print('[1] À vista no dinheiro ou cheque = 10% de desconto')
print('[2] À vista no cartão = 5% de desconto')
print('[3] Em até 2x no cartão = Sem desconto')
print('[4] Em 3x ou mais no cartão = 20% de juros')
forma = int(input('Digite a opção de pagamento: '))
if forma == 1:
    print(f'Com o desconto de 10%, o preço do produto é de R${preço * 0.9:.2f}')
elif forma == 2:
    print(f'Com o desconto de 5%, o preço do produto é de R${preço * 0.95:.2f}')
elif forma == 3:
    print(f'Com a forma de pagamento selecionada, o preço do produto continua sendo R${preço:.2f}')
elif forma == 4:
    parcela = int(input('Quantas parcelas? '))
    mensal = (preço / parcela) * 1.2
    print(f'Em {parcela} parcelas, o preço mensal do produto será de R${mensal:.2f}')
    print(f'O preço total passará de R${preço:.2f} para R${mensal * parcela:.2f}')
else:
    print('O número digitado é inválido')

