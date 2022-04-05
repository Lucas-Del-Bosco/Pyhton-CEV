print('Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.\nA multa vai custar R$7,00 por cada Km acima do limite.')

vel = float(input('Qual a velocidade do carro?: '))
if vel > 80:
    print(f'A sua velocidade ultrapassou o limite de 80km/h, por isso deverá pagar uma multa de R${(vel-80)*7:.2f}. ')
else:
    print('Tenha um BOM DIA!')

