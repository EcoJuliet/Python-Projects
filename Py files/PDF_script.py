#! python3

'''
OBJETIVO DO SCRIPT:

Pegar os seguintes arquivos PDF que são feitos nos faturamentos e colocá-los em
um só:

O arquivo de output deverá ser:

PRIMEIRO: - nota fiscal
SEGUNDO: - boleto
TERCEIRO: - arquivos escaneados da reserva.
'''

import PyPDF2
import os

os.chdir('\\\\ATENDIMENTO\\Users\\Usuario\\Desktop\\SCANNER PDF')
print ('DEBUG: '+os.getcwd())

print('''PDF Merger: O script combinará dois ou mais arquivos PDF em um novo.''')

print('Por favor digite o nome do primeiro arquivo: ')
pdf1File = open(input()+'.pdf', 'rb')

print('Agora, o do segundo arquivo: ')
pdf2File = open(input()+'.pdf', 'rb')

print('Por favor, digite o nome do terceiro aquivo: ')
pdf3File = open(input()+'.pdf', 'rb')

   
# comandos para combinar os arquivos.
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)
reader3 = PyPDF2.PdfFileReader(pdf3File)
writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
	page = reader1.getPage(pageNum)
	writer.addPage(page)

	
for pageNum in range(reader2.numPages):
	page = reader2.getPage(pageNum)
	writer.addPage(page)


for pageNum in range(reader3.numPages):
	page = reader3.getPage(pageNum)
	writer.addPage(page)

print('Digite o nome do arquivo de saida. Nao esqueça de colocar .pdf no final ;) ')	
	
outputFile = open(input()+'.pdf', 'wb') # 'wb' is writing in binary
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
pdf3File.close()

print('Pronto!')
print ('''DEBUG: \nObrigado por ter participado deste
teste patrocinado pela Apperture Science!''')

print('Script por: Eros Junior :)')
