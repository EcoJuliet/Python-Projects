print ('Você está em uma encruzilhada.')

def turn(direcao):
    if direcao == 'direita':
        print ('Virou à direita. Morreu PSDBista')
    elif direcao == 'esquerda':
        print ('Virou à esquerda. Morreu Petista.')
    else:
        print ('Não existe essa opção, colega.')


print ('Para qual lado você vira? [esquerda/direita] ')

direcao = input()
turn(direcao)

print ('Depois de ter virado à ', direcao, 'você ganhou superpoderes.')
