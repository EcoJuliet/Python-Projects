# TIC-TAC-TOE basico
''' duas ideias: a lista com os campos a serem preenchidos com X ou O,
e a 'mesinha'.
'''
# vou copiar o código que digitei no Automate the Boring Stuff...

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
		'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
	        'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

import pprint
#pprint.pprint(theBoard)  - para deixar mais fácil de ver.


# agora, a mesinha
def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-M'])
	print ('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-M'])
	print ('-----')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-M'])


