# STRING FORMATTING

'''
As strings podem ficar mais bonitas ao se usar o CONVERSION SPECIFIERS

Por exemplo:
'''
nome = 'Eros'
idade = '27 anos'
cidade = 'Socorro'
'''
% - conversion specifier
'''
print (nome + ' tem ' + str(idade) + ' anos e mora na cidade de ' + cidade)

'''
FICA MUITO MAIS BONITO ASSIM:
'''

print ('%s tem %s anos e mora na cidade de %s' % (nome, idade, cidade))


NÉ? SEXY
