qtd = input('Digite a quantidade desejada: ')
# preciso achar esses arquivos no computador, eles precisam de um nome!
# para qtd inserida, pegar os nomes
# para nome inserido, colocar os nomes em um arquivo pdfX para cada
# para qtd inserida, colocar os arquivos pdfX em um leitorX
# para cada leitor X:
# pegar o número de páginas e adicionar ao escritor geral.

import os
import PyPDF2

os.chdir('\\\\ATENDIMENTO\\Users\\Usuario\\Desktop\\SCANNER PDF')

print ('Digite os nomes dos arquivos a seguir: ')

nomes = []
for i in range(0,int(qtd)):
    i = input()
    nomes.append(i)
    
print (nomes)
pdf = []


for i in nomes:
    pdf.append(i)
        
print (pdf)
leitor = []

for i in pdf:
    open(i, 'rb')
    for i in pdf:
        leitor.append(i)

print (leitor)
exec = []

for i in leitor:
    leitor = PyPDF2.PdfFileReader(pdf)
    
for numPag in range(leitor):
    pagina = leitor.getPage(numPag)
    escritor.addPage(pagina)


'''
pdf1 = open(input()+'.pdf', 'rb')		 # nome do arquivo PDF que escaneei.
leitor1 = PyPDF2.PdfFileReader(pdf1)	 # objeto leitor (necessário)
print()
for numPag in range(leitor1.numPages):   # para cada página do objeto leitor...
    pagina = leitor1.getPage(numPag)	 # pega o número dela...
    escritor.addPage(pagina)			 # e adiciona no escritor...
'''

print()
print('Digite o nome do arquivo de saida ;) - SEM PDF ')	
arquivoSaida = open(input()+'.pdf', 'wb') # 'wb' is writing in binary
print()
print('Só um momento por favor! ')
print('...')
print()
escritor.write(arquivoSaida)
arquivoSaida.close()
for i in pdf:
    pdf.close()
print('Pronto!')
print('\n'*3)   
print ('Obrigado por ter participado neste exercicio patrocinado pela Apperture Science!')
print()
print('Script por: Eros Junior :)')

    
