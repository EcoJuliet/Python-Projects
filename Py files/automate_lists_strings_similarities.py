# Strings and lists are very similar

DIFERENÇAS:
STRINGS = immutable data types
LISTS = mutable data types

A melhor forma de modificar uma string, é criar uma nova string usando slices[x:y]E
EXEMPLO:
    
>>> name = 'Zophie a cat'
>>> name[0:7]
'Zophie '
>>> name[0:7] + 'the' +name[8:]
'Zophie the cat'

# -------------------------------
A DIFERENÇA ESTA NA REFERENCIAS

# VARIABLES DON'T CONTAIN LISTS PER SE, THEY CONTAIN REFERENCES TO THE LIST!

>>> spam = [0, 1, 2, 3, 4, 5]
>>> cheese = spam
>>> cheese
[0, 1, 2, 3, 4, 5]
>>> cheese[1] = 'ONE'
>>> cheese
[0, 'ONE', 2, 3, 4, 5]
>>> spam
[0, 'ONE', 2, 3, 4, 5]
>>> 
MINDFUCK
'''
YOU DON'T STORE MUTABLE VALUES ON VARIABLES, YOU STORE REFERENCES.
IMMUTABLE VARIABLES ARE OK. BECAUSE THEY CAN ONLY BE REPLACED BY A NEW VALUE!
'''


# ------------------
DEEP COPY

o Python tem uma função nata chamada "COPY"
acessada por
import copy
Ela tem uma subfunção chamada DEEPCOPY, que nao copia somente a referência à lista,
mas sim a lista toda.

Assim:

>>> lista1 = ["a", "b", "c", "d"]
>>> lista2 = [1, 2, 3, 45]
>>> lista1 = copy.deepcopy(lista2)
>>> lista1
[1, 2, 3, 45]
>>> lista2
[1, 2, 3, 45]
>>> lista1[0] = 'BACON'
>>> lista1
['BACON', 2, 3, 45]
>>> lista2
[1, 2, 3, 45]


 
