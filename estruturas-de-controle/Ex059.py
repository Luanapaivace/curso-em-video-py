from math import factorial
n = int(input("Digite um número inteiro e descubra o seu fatorial: "))
c = n
f = 1
print("Calculando {}! =".format(n), end="")
while c > 0:
    print(" {}  x ".format(c), end="")
    print(""if c > 1 else " = ", end="")
    f *= c
    c -= 1
print("{}".format(f))
    