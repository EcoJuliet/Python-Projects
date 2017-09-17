#FUNCTIONS

# function 'Hello'
'''
def hello():
    print ('HII')
    print ('OH HAI HELLO')
    print ('He-llooo'+'o'*3)

hello()
hello()
'''

#STRUCTURE OF A FUNCTION:
#def function(parameter/variable)
#   body
#   body
#function(argument)

# The input to functions are arguments
# The output is the RETURN value
# Every function has a return value, if it doesn't show, it's "None".


'''
def -> DEFines a function
function -> its name
parameter/variable ->
body ->
function(argument) -> calls the function and execute it.
(argument) -> is assigned by the parameter.
'''
# EXAMPLE:
'''
def hello(name):
    print('hello ' + name)

hello('Alice')
hello('Bob')
'''
'''
# EXAMPLE 2:
def plus_one(number):
    return number + 1

plus_one(5)
new_number = plus_one(5)
print (new_number)
'''
# DICA: PRINT SEM VALOR () <- sempre retorna 'None'
'''
se eu fizer:
    spam = print()
    spam == None
    o resultado é: True
'''
