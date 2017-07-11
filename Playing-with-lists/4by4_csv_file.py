# UMA LISTA 4x4 NUM ARQUIVO .CSV QUALQUER

# PARECE MUSICA


#TODO: Fazer uma lista de 4x4 com números crescentes

lista_de_listas = []



# PRIMEIRA SUBLISTA
for i in range(1):
    sublista1 = []
    lista_de_listas.append(sublista1)
    x = 0
    for i in range(4):
        x += 1
        sublista1.append(x)
        
# SEGUNDA SUBLISTA
for i in range(1):
    sublista2 = []
    lista_de_listas.append(sublista2)
    x = 4
    for i in range(4):
        x += 1
        sublista2.append(x)

# TERCEIRA SUBLISTA
for i in range(1):
    sublista3 = []
    lista_de_listas.append(sublista3)
    x = 8
    for i in range(4):
        x += 1
        sublista3.append(x)
      


# QUARTA SUBLISTA
for i in range(1):
    sublista4 = []
    lista_de_listas.append(sublista4)
    x = 12
    for i in range(4):
        x += 1
        sublista4.append(x)
        



    
''' 
print('DEBUG:')
print('DEBUG: SUBLISTAS')
print('SUBLISTA 1: ' + str(sublista1))
print('SUBLISTA 2: ' + str(sublista2))
print('SUBLISTA 3: ' + str(sublista3))
print('SUBLISTA 4: ' + str(sublista4))
print('DEBUG: LISTA DE LISTAS')
'''
print(lista_de_listas)


#TODO: CRIAR UM ARQUIVO CSV lindo
import os

# lista_de_listas = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

Bertuga = open('nome_generico.csv', 'a')

#TODO: ADICIONAR A LISTA 4X4 DE QUALQUER COISA
for i in lista_de_listas:
    for i in i:
        Bertuga.write((str(i)))
        Bertuga.write('\n')
#TODO FECHAR O ARQUIVO.
Bertuga.close()

print('DONE')

# COMENTÁRIO: NOVA LINHA É UMA PRAGA.

