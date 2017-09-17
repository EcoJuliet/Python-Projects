# For Loops


# Example 1
'''
print ('My name is ')
for i in range(5):
    print ('Jimmy Five Times ' + str(i)+1)
    # i começa no range 0!
'''

# Example 2: sum numbers from 0 to 100
'''
total = 0
for num in range (101):
    total = total + num
print (total)
'''

# COMENTARIOS SOBRE RANGE
'''
range() -> ACEITA TRÊS ARGUMENTOS
(x, y, z)
x -> de onde começa: padrão 0.
y -> até onde vai, MAS NÂO INCLUSO.
z -> de "quanto em quanto" ele sobe.
'''

# COMENTARIOS:
# break e continue ainda dá pra usar.

# SOMA GAME:
''' SE O USUARIO COLOCA 0, CHAMA DE BURRO.
SE ELE INSERE UM OUTRO NÚMERO, SOMA TODOS OS NÚMEROS ATE O DELE'''

user_name = input('ESCREVE O NOMEZIM AQUI, FA FAVÔ: ')
user_name = user_name.upper()
print (('VALEW, %s') % user_name)


total = 0
for num in range(int(input('INSIRA UM NUMERO QUALQUER (meno zero) :'))+1):
# O +1 é importante, pois o range NAO INCLUE A ULTIMA ITERAÇÃO.
# ele vai dentro do RANGE
    total = total + num
    
if total == 0:
    print ('EU FALEI MENO ZERO SEU BURRO!')
print (total)

