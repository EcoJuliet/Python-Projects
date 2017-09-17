#! python3
#shebang line /\


# mimimi generator

print ("Digite o texto a ser 'mimimizado'")
texto = input()

def mimi(texto):
    texto.lower()
    texto_novo = texto.replace('a', 'i').replace('e', 'i').replace('o', 'i').upper()
    print ("") 
    print ('NOVO TEXTO:') 
    print (texto_novo)

    
mimi(texto)

