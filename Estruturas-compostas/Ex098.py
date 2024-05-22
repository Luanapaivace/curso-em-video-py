def maior(*num):
    tam = len(num)
    print(f"Recebi os valores{num}, são ao todo {tam} e o maior número foi o {max(num)}")


maior(1, 2, 5, 6)
maior(9, 1, 4)