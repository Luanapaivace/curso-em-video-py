def aumentar(preco = 0):
    res = preco + (preco * 10/100)
    return res

def diminuir(preco = 0):
    res = preco - (preco * 10/100)
    return res

def dobrar(preco = 0):
    res = preco * 2
    return res

def meta(preco = 0):
    res = preco / 2
    return res


def moedaz(preco = 0, moedaz = "R$"):
    return f"{moedaz}{preco:.2f}".replace(".", ",")