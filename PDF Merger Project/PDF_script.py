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
print ('PATH de entrada e saida: '+os.getcwd())
print('\n'*2)
print('---------------------')
print('PDF Merger: O script combinará três arquivos PDF em um novo.')
print('---------------------')
print('Por favor digite o nome do primeiro arquivo (não precisa de ".pdf ;)": ')
pdf1 = open(input()+'.pdf', 'rb')
print()
print('Agora, o do segundo arquivo: ')
pdf2 = open(input()+'.pdf', 'rb')
print()
print('Por favor, digite o nome do terceiro aquivo: ')
pdf3 = open(input()+'.pdf', 'rb')

   
# comandos para combinar os arquivos.
leitor1 = PyPDF2.PdfFileReader(pdf1)
leitor2 = PyPDF2.PdfFileReader(pdf2)
leitor3 = PyPDF2.PdfFileReader(pdf3)
escritor = PyPDF2.PdfFileWriter()

for numPag in range(leitor1.numPages):
	pagina = leitor1.getPage(numPag)
	escritor.addPage(pagina)

	
for numPag in range(leitor2.numPages):
	pagina = leitor2.getPage(numPag)
	escritor.addPage(pagina)


for numPag in range(leitor3.numPages):
	pagina = leitor3.getPage(numPag)
	escritor.addPage(pagina)
	
print()
print('Digite o nome do arquivo de saida ;) ')	
arquivoSaida = open(input()+'.pdf', 'wb') # 'wb' is writing in binary
print()
print('Só um momento por favor! ')
print('...')
print()
escritor.write(arquivoSaida)
arquivoSaida.close()
pdf1.close()
pdf2.close()
pdf3.close()
print('Pronto!')
print('\n'*3)   
print ('Obrigado por ter participado neste exercicio patrocinado pela Apperture Science!')
print()
print('Script por: Eros Junior :)')
