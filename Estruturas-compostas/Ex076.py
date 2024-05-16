pala = ("Garrafa", "Escola", "Cidade", "Casa", "Padaria")
for p in pala:
    print(f"\nNa palavra {p.upper()} temos ", end=" ")
    for le in p:
        if le.lower() in "aeiou":
            print(le, end=" ")