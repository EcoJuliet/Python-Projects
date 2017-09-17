# NERD TRUE OR FALSE TEST

def nerd():
    print("O usuário é nerd? [S/N]")

    nerd = input()
    if nerd == 's' or nerd == "sim":
        print("O usuário É nerd, portanto, \nNão faltaras!!")
    elif nerd == 'n' or nerd == "nao":
        print("O usuário NAO É nerd, dessa forma, \nFaltarás!")
    else:
          print('Responda certo, cacete!')

nerd()
