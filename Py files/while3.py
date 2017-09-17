# Algoritimo: Soma números
# mostra a soma dos números inseridos

contador = 1
soma = 0
while (contador <= 5):
    print ("Digite o",str(contador),"º. valor")
    numero = int ( input ())
    soma = soma + numero
    contador = contador + 1

print ("A soma dos números foi", soma)
