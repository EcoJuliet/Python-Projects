
# LESSON 30 - FILES AND FOLDERS

Two important concepts:
    FILENAMES - o nome do troço
    AND
    FILE PATHS - onde o troço ta.
    FILE EXTENTION - .png, .jpg, .txt

    C:\ - root folder.

    LEMBRETE - no Python, como o \ serve com o "escape", eu tenho que digitar 2
    backlashes pra fazer sentido. EXEMPLO:
        >>> 'c:\\users\\usuario\\pasta'

    OU: usar raw strings:
        >>> r'c:\users\usuario\pasta'

        NO WINDOWS - da para usar o .join() method para juntar o endereço.
        EXEMPLO:
            '\\'.join(['pasta1', 'subpasta2', 'subpasta3', 'arquivo.jpg'])
            # ESSE CODIGO SÓ FUNCIONARIA NO WINDOWS.

# -------------- usar o módulo OS.
Módulo para juntar o caminho:
os.path.join('pasta1', 'subpasta2', 'subpasta3', 'arquivo.jpg')

os.getcwd() # para ver o caminho da pasta de trabalho
os.chdir() # para mudar o caminho da pasta de trabalho atual

# ABSOLUTE AND RELATIVE PATHS

ABSOLUTE FILE PATH: a posição COMPLETA do arquivo.
'C:\\user\\usuario\\file.png'
#C: root folder
RELATIVE FILE PATH: é relativo ao local do arquivo.
considera que esta dentro da root folder:
'folder1\\folder2\\spam.png'

# SPECIAL FOLDERS
. - this directory folder
..- the parent folder.

# MORE COMMANDS
os.path.abspath('ARQUIVO') # vai devolver o caminho absoluto de um arquivo dado
                           # em caminho relativo pelo CWD!

os.path.isabs()            # recebe um endereço qualquer e retorna se e absoluto
                           # ou nao

os.path.relpath(TO, FROM)   # retorna o caminho relativo FROM algum caminho
                            # TO outro caminho.

os.path.dirname(ARQUIVO ABSOLUTO) # retorna o diretório do arquivo
os.path.basename(ARQUIVO ABSOLUTO) # retorna o arquivo sem o diretorio

os.path.exists(FILE PATH) # retorna se o filepath existe ou nao.
os.path.isfile()    # parecido, mas com arquivos.
os.path.isdir()     # parecido, mas com diretórios.

os.path.getsize(ABSOLUTE FILE) # retorna o tamanho doarquivo em bytes

os.listdir(PASTA) # retorna todos os arquivos de uma pasta em strings


PROGRAMA EXEMPLO:
VER O TAMANHO DE TODOS OS ARQUIVOS EM UMA PASTA
# ----------------

import os
totalSize = 0 # pra começar com 0, importante.
for filename in os.listdir('C:\\Users\\Usuario\\Desktop\\Textos'): # ... no diretorio TAL
    if not os.path.isfile(os.path.join('C:\\Users\\Usuario\\Desktop\\Textos', filename)): # se nao for "arquivo"
        continue # continuar
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\Usuario\\Desktop\\Textos', filename)) # se for, somar

print (totalSize)
# FUNCIONA!
# -----------------

CREATE FOLDERS:
    os.makedir('NOME DAS PASTAS QUE QUER CRIAR') # CRIAR PASTAAAAS
