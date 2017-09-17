# LESSON 31: READING AND WRITING FILES

Types of files well be reading and writing: plaintext and Binary Files

plaintext: .txt
binary files: anything else. - doesnt open properly on notepad.

# THREE STEPS TO WRITTING ANG READING FILES ON PYTHN.

'''
1 - open(FILENAME) function.
'''
The open function only lets you use the "READ-ONLY" mode of the file
THE FUNCTION SAVES IT TO A 'FILE OBJECT'.
PUT IT IN A SYNTAX

The FILE OBJECT has many of methods.
.read()  - # reads the file. Reads only once.
.close() - # closes the damn thing
.readlines() - # returns all lines as strings inside a list.

To write information in a file, you have to open it in
write mode. # HOW? open(FILE, 'w') # rewrite the file
or         # open(FILE, 'a')
append mode. # append the info in the existing file

FILENAME.write() # write information

# NOTE: Write mode doesn't automatically adds a new line to a text file.
# NOTE 2: SEM O FILE PATH COMPLETO, O PYTHON VAI USAR O CWD (OS MODULE) PRA TRABALHAR.

Shelve MODULE. # para outros que nao são plaintext
import shelve
# it has a dictionary-like structure
shelve.open('mydata') - retorna um SHELVE file object
ShelFile = shelve.open('mydata')
ShelFile['dogos'] = ['Flibers', 'Todi', 'Bunfo', 'Banano']
ShelFile.close()
# posso reabrir e ver que os arquivos ainda existem.
ShelFile = shelve.open('mydata')
ShelFile['dogos']
RETORNA: ['Flibers', 'Todi', 'Bunfo', 'Banano']
'''
O 'mydata' na verdade são 3 arquivos. NO WINDOWS:
    mydata.bak
    mydata.dir
    mydata.dat
'''

SHELF FILES are very similar to dictionaries. THEY ARE SO SIMILAR, that
they have
list(ShelfFile.keys()) # returns a list of the keys, like a dictionary
and
list(ShelfFile.values()) # returns a list of values, like a dictionary
methods.


