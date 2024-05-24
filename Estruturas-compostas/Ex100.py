from datetime import date
def voto(ano):
    atu = date.today().year
    ida = atu - ano
    if ida < 16:
        return f"Com {ida} anos: Não vota!"
    elif 16 <= ida < 18 or ida > 65:
        return f"Com {ida} anos: Voto opcional"
    else:
        return f"Com {ida} anos: Voto obrigatorio"
    
ani = int(input("Ano de nascimento: "))
print(voto(ani))