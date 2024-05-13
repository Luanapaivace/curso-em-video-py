import math
l1 = float(input("Digite o primeiro lado do triângulo: "))
l2 = float(input("Digite o segundo lado do triângulo: "))
l3 = float(input("Digite o terceiro lado do triângulo: "))
if l1 < l2 + l3 and l2 < l1 < l3 and l3 < l1 + l2:
    print("Os valores a cima podem formar um triângulo")
    if l1 == l2 == l3:
        print("Equilatéro")
    if l1 != l2 != l3:
        print("Escaleno")
    else:
        print("Isóceles")
else:
    print("Os valores a cima não podem formar um triângulo")
