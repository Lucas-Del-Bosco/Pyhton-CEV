print('Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:\n– Média abaixo de 5.0: REPROVADO\n– Média entre 5.0 e 6.9: RECUPERAÇÃO\n– Média 7.0 ou superior: APROVADO')

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'A sua média final é \33[34m{media:.2f}\33[m.\nStatus: \33[31mREPROVADO!\33[m')
elif 5 <= media < 7:
    print(f'A sua média final é \33[34m{media:.2f}\33[m \nStatus: \33[33mRECUPERAÇÃO!\33[m')
elif media >= 7:
    print(f'A sua média final é \33[34m{media:.2f}\33[m. \nStatus: \33[32mAPROVADO!\33[m')