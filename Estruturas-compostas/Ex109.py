def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número válido inteiro.\033[m")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário")
            return 0
        else:
            return n
        
        
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número válido inteiro.\033[m")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário")
            return 0
        else:
            return n


n1 = leiaint("Digite um valor: ")
n2 = leiafloat("Digite um número real: ")
print(f"O valor digitado foi: {n1} e {n2}")