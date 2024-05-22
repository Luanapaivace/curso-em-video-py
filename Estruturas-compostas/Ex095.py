def vezes(a, b):
    v = a * b
    print(f"A área de um terreno {a}x{b} é igual a {v}")


print("Controle de terrenos")
print("-=-" * 7)
larg = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))
vezes(larg, comp)