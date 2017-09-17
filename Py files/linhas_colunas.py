'''
>>> for i in range(3):
	temp = []
	for j in range(3):
		temp.append('x')
	board.append(temp)

	
>>> for i in board:
	print (i)

	
['x', 'x', 'x']
['x', 'x', 'x']
['x', 'x', 'x']
>>> for i in board:
	print (''.join(i))

	
xxx
xxx
xxx

import pprint
lista = []
meta = int(input())
for i in range(0,meta):
    x = []
    x.append('x')
    for j in x:
        lista.append(x*meta)
        

pprint.pprint(lista)
'''    
import pprint
print ('Por favor, insira um número qualquer igual ou maior de 3: ')
qtd = int(input()) # pedir pro usuário. MEXER NELE, PRA ACEITAR SÓ NUMEROS A MAIS DE 3
xises = [] # grupo vazio que vai entrar grupos de x aqui.

if qtd < 3:
    print ('EU DISSE IGUAL OU MAIOR QUE TRÊS, CARALHO!\n'*qtd*10)
elif qtd >= 3:
  
    for i in range(qtd): # não POSSO colocar no grupo, preciso usar o range dele.
            linhas = [] # uma lista para serem colocadas as linhas, dentro do grupo 'xises'
            for k in range(qtd): # pra cada iteração da lista de dentro...
                linhas.append('x') # alguma hora tenho que colocar os x né?
            xises.append(linhas) # adiciono as linhas no grupo xises?
'''	
print ('DEBUG')
print (xises) # só pra ter certeza que tá saindo certo
print ('END OF DEBUG')
'''
print ('')
for i in xises:
	print(''.join(i)) # De acordo com o AUTOMATE, é pra tirar de listas e imprimir em strings, separadas por espaço em branco.
print ('')	
print ('Fim da execução \n')


    
