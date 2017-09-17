'''

enquanto o número digitado não for maior q 1, pedir pro cara digitar um número                        
nas extremidades, trocar os caracteres por barras                        
exemplo                        
3                        
\X/
XXX
/X\

'''

meta = int(input())

contador = 0

    while (contador < meta):
        print ('\\'*(meta-1))
        print ('X'*(meta))
        print ('/'*(meta-1))

        contador = contador + 1
    
