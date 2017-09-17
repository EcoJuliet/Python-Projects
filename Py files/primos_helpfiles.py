# L: 18 print (numero, 'é igual a ', outro_numero, '*', numero//outro_numero)
print ('--------------------------')
print ('BUSCADOR DE NUMEROS PRIMOS')
print ('--------------------------')

print ('Favor insira um número: ')

# VARIAVEIS

primo = int (input ())
soma = 0                                # vergonha completa de não ter lembrado disso
# CODIGO

for numero in range (2, primo): 
    ''' função: buscar uma lista de números primos abaixo do número inserido. Somar eles '''
    for outro_numero in range(2, numero):
        
        if numero % outro_numero == 0:  # Elimina os não-primos (divisíveis entre si)!
            soma = numero + soma        # piranha desgraça                  
            break                       # Não precisa do Else agora.
    else:                               # e essa bosta pertence ao FOR, não ao IF/ for não tem else
        print (numero, 'é primo')

print ("A soma dos números primos abaixo do número inserido é:", soma)

print ('--------------------------')
print ('FIM DA EXECUÇÃO DO CODIGO')

print ('''PS: Achei essa belezinha nos Help Files do próprio Python.
Não procurei no Google!''')
