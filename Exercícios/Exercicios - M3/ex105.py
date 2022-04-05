#print('Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:\n– Quantidade de notas\n– A maior nota\n– A menor nota\n– A média da turma\n– A situação (opcional)')

def notas(*num, sit=False):
    '''
    -> Panorama geral de notas em uma turma.
    :param num: Notas a serem consideradas.
    :param sit: (opcional), mostra o status da turma.
    :return: O dicionário com todas as informações.
    '''
    ng = dict()
    ng['total'] = len(num)
    ng['maior'] = max(num)
    ng['menor'] = min(num)
    ng['média'] = sum(num)/len(num)
    if sit:
        if ng['média'] > 6:
            ng['situação'] = 'BOA'
        else:
            ng['situação'] = 'RUIM'
    return ng


#Programa Principal
resp = notas(7.5, 3.5, 10, sit=True)
print(resp)
help(notas)
