def aumentar(preço=0, taxa=0, formato=False):
    desconto = preço * taxa/100
    total = preço + desconto
    return total if formato is False else moeda(total)


def diminuir(preço=0, taxa=0, formato=False):
    desconto = preço * taxa/100
    total = preço - desconto
    return total if formato is False else moeda(total)


def dobro(preço=0, formato=False):
    total = preço * 2
    return total if not formato else moeda(total)


def metade(preço=0, formato=False):
    total = preço / 2
    return total if not formato else moeda(total)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: {aumentar(preço, taxaa, True)}')
    print(f'Com {taxar}% de redução: {diminuir(preço, taxar, True)}')
    print('-' * 30)

