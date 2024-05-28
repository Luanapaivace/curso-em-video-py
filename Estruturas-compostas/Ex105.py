def cabecalho(msg, cor=0):
    if cor == 1:
        print('\033[97;42m', end='')
    if cor == 2:
        print('\033[97;44m', end='')
    if cor == 0 or cor > 2:
        print('\033[m', end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}  ')
    print('~' * (len(msg) + 4))


def ajuda(aju):
    cabecalho(f"Acessando o manual do comando '{aju}'.", 2)
    print('\033[30;107m', end='')
    help(aju)


while True:
    cabecalho('Sistema de Ajuda Python', 1)
    fun = input('\033[mFunção ou Biblioteca > ').lower().strip()
    if fun == 'fim':
        break
    ajuda(fun)