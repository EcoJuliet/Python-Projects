# lesson 34 - WALKING A DIRECTORY TREE

'''
Fazer algo em todos os arquivos e subpastas em uma pasta.
'''
'''
Inside the OS MODULE
os.walk(PATH) # function
A função é usar no FOR LOOP.

Como é um for loop, você pode nomear qualquer merda nas variables.

EXEMPLO:
A ordem será essa:
    '''
for folderName, subfolders, files in os.walk('C:\\Users\\Usuario\\Desktop\\Textos'):
	print("The folder is "+ folderName)
	print("The subfolders in "+ folderName + "are " + str(subfolders))
	print("The files in "+ folderName + "are " + str(files))
	print()
#subfolders é uma LISTA
#filenames é uma LISTA

# Para cada iteração dentro de cada pasta, sera impresso isso.
