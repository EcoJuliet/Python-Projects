# Verificar quantos valores estão entre 0 e 10

tot010 = 0
c = 1


for C in range (1,6):
    print ('Por favor escreva um valor')
    v = int(input())
    if (v >= 0) and (v <= 10):
        tot010 = tot010 + 1


print ('Ao todo foram ', tot010, 'valores entre 0 e 10')
        
