print("-=-" * 7)
print("10 termos de uma PA")
print("-=-" * 7)
t = int(input("primeiro termo: "))
r = int(input("razão: "))
for c in range(t, 20, r):
    print("{}".format(c), end= ",")
print("Acabou")