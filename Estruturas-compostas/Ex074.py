n1 = tuple(int(input("Digite um número inteiro: "))for c in range(1, 5))
print(f"Você digitou os números {n1}")
if 9 in n1:
     print("O valor 9 foi digitado {} vezes".format(n1.count(9)))
else:
     print("O valor 9 não foi digitado")
if 3 in n1:
     print("O valor 3 foi digitada na {} posição".format(n1.index(3)+1))
else:
     print("O valor 3 não foi digitado")
print("Os números digitados e que foram par:", end=" ")
for n in n1:
     if n % 2 == 0:
          print(n, end=" ")