fi = list()
while True:
    nome = str(input("Digite o seu nome: "))
    n1 = float(input("Digite a sua nota: "))
    n2 = float(input("Digite outra nota sua: "))
    m = (n1 + n2) / 2
    fi.append([nome, [n1, n2], m])
    r = str(input("Quer continuar? "))
    if r in "Nn":
        break
print("-=-" * 30)
print(f"{"No.":<4}{"Nome":<10}{"Média":<8}")
print("-=-" * 30)
for i, a in enumerate(fi):
    print(f"{i:<4}{a[0]:<10}{a[2]:<8.1f}")
while True:
    print("-=-" * 30)
    opc = int(input("Mostrar nota de qual aluno? [999 para interromper]"))
    if opc == 999:
        print("Finalizando...")
        break
    if opc <= len(fi) - 1:
        print(f"Notas de {fi[opc][0]} são {fi[opc][1]}")
print("FIM")