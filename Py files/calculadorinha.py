import operator
print ('------------------------------')
print ('Calculadorinha formato peasant')
print ('------------------------------')
# as variáveis
x = int(input ('Digite o primeiro número: '))
operador = input ('Selecione um operador: + - / *: ')
y = int(input('Digite o segundo número: '))
# o shumbalaio
if operador == '+':
    print (operator.add(x,y))
elif operador == '-':
    print (operator.sub (x,y))
elif operador == '/':
    print (operator.truediv(x,y))
elif operador == '*':
    print (operator.mul(x,y))
else:
    print ('ESCOLHA UMA OPÇÃO DECENTE, POR FAVOR')


print ('Pronto!')
