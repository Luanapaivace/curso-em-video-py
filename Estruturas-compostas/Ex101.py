def fatorial(n, show=False):
    """
    -> calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=" ")
            if c > 1:
                print(" x ", end=" ")
            else:
                print(" = ", end=" ")
        f *= c
    return f
print(fatorial(5, show=True))