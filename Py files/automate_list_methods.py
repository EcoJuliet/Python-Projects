# LIST METHODS (aula 15):

'''
TO FIND THE INDEX OF A LIST, WE CAN USE THE METHOD list_name.index(item)
let's say:
'''
spam = ['hello', 'hi', 'howdy', 'heyas', 'oi']
spam.index('Hello')
# expected result: 0
spam.index('heyas')
# expected result: 3

# ------------------------------------------
eggs = ['arroz', 'carne', 'feijao', 'bacon', 'banana', 'arroz']
# em uma lista com duplicatas, como essa.
eggs.index('arroz')
# só retorna a PRIMEIRA VEZ que o item aparece na lista

# ------------------------------------------
'''
lista.append() -> adiciona um objeto no final da lista
lista.insert(index, object) -> adiciona um objeto no index que eu quero da lista
'''
spam.append('ciao') # adiciona 'ciao' no final da lista spam lá em cima
spam.insert (1, 'aloha') # adiciona 'aloha', no index 1 da lista, move os outros para frente

# esses método so podem ser chamados em LISTAS

# -----------------------------------------
'''
lista.remove(object) -> remove um item de uma lista.
ESSE METODO REMOVE SÓ A PRIMEIRA REPETICAO DA LISTA
del lista(index) -> é diferente, porque remove o índex
'''
# -----------------------------------------
# listas com valores numéticos e strings podem ser organizadas pelo:
'''
lista.sort() -> organiza em ordem ou 'reverse = True', ordem reversa uma lista!
'''
fart = [1, 2, 65, 123, 643, 135, 3.15, 1663]
fart.sort()
fart = [1, 2, 3.15, 65, 123, 135, 643, 1663] # organizado!

# -----------------------------------------
'''
O Python usa o algoritmo ASCII para organizar as listas.
Todas as palavras que começam com maiúsculas são colocadas antes das que
iniciam com minúsculas
'''
nomes_e_bichos = ['Alice', 'alce', 'Bob', 'bobcat', 'Bacon', 'bacon']
nomes_e_bichos.sort()
nomes_e_bichos = ['Alice', 'Bacon', 'Bob', 'alce', 'bacon', 'bobcat']
# INTENSO.

'''
Para lidar com isso, precisamos passar o argumento 'key' na lista.'''
nomes_e_bichos.sort(key=str.lower) # organiza por ordem alfabetica


.join () - junta as treta tudo em string

