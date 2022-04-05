print('Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.\nA prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.')

casa = float(input('Qual é o valor da casa?: '))
salario = float(input('Qual é o valor do seu salário mensal?: '))
tempo = float(input('Em quantos anos você quer pagar essa casa?: '))
meses = tempo * 12
custo = casa / meses
if custo > salario * 0.3:
    print(f'O empréstimo não pode ser realizado pois o valor mensal é de {custo:.2f}, e portanto, maior que 30% do seu salário de {salario:.2f}!')
else:
    print(f'Você pagará {custo:.2f}, mensalmente!')