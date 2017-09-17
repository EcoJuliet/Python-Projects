# for Loops com listas

for i in range(0,4): == for i in range [0,1,2,3]:
   print (i)

Vai gerar:
0
1
2
3

# POR QUE?
'''
o 'for' loop vai dar ao 'i', o valor que esta dentro da lista, ou do range,
e vai imprimir esse valor.'''

for i in ['maçã', 'banana', 'pêra']:
    print (i)
#RESULTADO:
'maçã'
'banana'
'pêra'
# INCRÍVEL!

# LIST FUNCTION
''' para criar uma lista de uma função range, podemos usar a função "list()"
nesse caso'''
list(range(4)) == [0, 1, 2, 3] = True

# FOR i in range(len(AlgumaLista) COMMAND:,
supplies = ['pens', 'staplers', 'flamw-throwers', 'binders']
 for i in range(len(supplies)):
	print ('Index' + str(i) + ' in supplies is: '+ supplies[i])
	
''' EXPECTED RESULT:
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamw-throwers
Index 3 in supplies is: binders
'''

# OUTRO:
shopping_list = ['arroz', 'feijao', 'carne', 'doces', 'café', 'açucar', 'leite', 'leite dcondensado', 'almondegas', b'ananas', 'maças', 'peras', 'economia', 'feijoada', 'peixes', 'tomate', 'tomilho', 'filmes']

for i in range(len(shopping_list)):
	print (str(i), shopping_list[i])

''' expected result:
0 arroz
1 feijao
2 carne
3 doces
4 café
5 açucar
6 leite
7 leite dcondensado
8 almondegas
9 b'ananas'
10 maças
11 peras
12 economia
13 feijoada
14 peixes
15 tomate
16 tomilho
17 filmes
'''


# MULTIPLE ASSIGNMENTS:
'''
O Python pode nomear várias variáveis em base de uma lista ao mesmo tempo.
Por exemplo:
'''
food = ['arroz','feijao', 'carne']
principal, acompanhamento, mistura = food

'''RESULTADO ESPERADO:
principal = 'arroz'
acompanhamento = 'feijao'
mistura = 'carne'
'''
# da hora.



# VARIABLE SWAP
a = 'AAA'
b = 'BBB'

a, b = b, a # significa: agora a = b e b = a
'''
EXPECTED RESULT:
a = 'BBB'
b = 'AAA'
'''


# AUGMENTED ASSIGNMENTS:
''' Atalhos para
spam = spam + 1
'''
spam += 1 # = spam = spam + 1
spam -= 1 # = spam = spam - 1
spam /= 1 # = spam = spam / 1
spam *= 1 # = spam = spam * 1
spam %= 1 # = spam = spam % 1
'''





