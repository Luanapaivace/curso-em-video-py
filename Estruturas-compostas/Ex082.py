ep = str(input("Digite uma expressão matematica: "))
p = []
for simb in ep:
    if simb == "(":
        p.append("(")
    elif simb == ")":
        if len(p) > 0:
            p.pop()
        else:
            p.append(")")
            break
if len(p) == 0:
    print("Está tudo correto")
else:
    print("Está errada :(")