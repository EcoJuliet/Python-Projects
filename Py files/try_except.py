def div42by(divideBy):
    try:
        return 42 / divideBy
    except: # this one skips all kinds of errors and shows 'none' + the print
        print ("Error: You tried to divide by zero, dumbass")

print (div42by(2))
print (div42by(12))
print (div42by(0))
print (div42by(1))

