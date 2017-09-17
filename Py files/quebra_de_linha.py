'''print('isso aqui vai quebrar a linha no fim')

print('esse não ', end="")
print('e nem esse', end="")
'''
'''def bingola(tamanho):
    if tamanho == 0:
        print ('japonês')
    return



tamanho = int(input('Insira o tamanho da bingola que você gostaria de ter, salafrário: '))
bingola(tamanho)
'''

def bingola(tamanho):
    if tamanho == 0:
        print ('japonês')
    else:
        #aqui a magia acontece
        #primeiro vc imprime o '8', mas sem quebrar a linha no fim
        print ('8', end="")
        #mais magia acontece aqui
        #aqui vc vai ter que fazer um laço, que começa no 1, e termina no tamanho
        for numero in range(1,tamanho+1): #
            print ('=', end="") #aff, jura?
        
        print ('D', end="")
        #isso ae :)
        # :)
    return



tamanho = int(input('Insira o tamanho da bingola que você gostaria de ter, salafrário: '))#lembrete: não aceita letras
bingola(tamanho)
