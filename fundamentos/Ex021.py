nome = str(input("Digite o seu nome: "))
print("O seu nome com as letras todas maiúsculas fica: {}".format(nome.upper()))
print("O seu nome com as letras todas minúsculas fica: {}".format(nome.lower()))
print("O seu nome tem {} letras".format(len(nome) - nome.count(' ')))
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))
