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
