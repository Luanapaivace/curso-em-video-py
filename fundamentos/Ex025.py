palavra = str(input("Digite uma frase ")).upper().strip()
print("A letra A aparece {} vezes na frase".format(palavra.count('A')))
print("A primeira letra A paraceu ns posição {}".format(palavra.find('A')+1))
print("A última letra A apareceu na posição {}".format(palavra.rfind('A')+1))