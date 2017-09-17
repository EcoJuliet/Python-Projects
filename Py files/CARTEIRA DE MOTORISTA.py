# CALCULAR A IDADE DA PESSOA E VER SE ELA PODE TIRAR A CARTEIRA DE MOTORISTA

from datetime import datetime

print ('-----------------------')
print ('DEPARTAMENTO DE TRÂNSITO')
print ('-----------------------')
now = datetime.now()
print ('Nós estamos em', now.year)
ano_nasci = int(input('Insira seu ano de nascimento (yyyy): '))

print ('------STATUS----------')

print ('IDADE: ', now.year - ano_nasci)
if now.year - ano_nasci >= 18:
    print ('APTO A TIRAR A CARTEIRA DE MOTORISTA')
else:
    print ('Por favor, aguarde até ter 18 anos.')
    
print ('---------------------')
