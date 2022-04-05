print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.\nPara salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.')

salario = float(input('Qual é o seu salário?: R$'))
if salario <= 1250.00:
    aumento = salario * 1.15
else:
    aumento = salario * 1.1
print(f'De acordo com o seu salário atual, o reajuste salarial fará com que passe a R${aumento:.2f}')
