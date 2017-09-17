# If statements
'''name = 'Alice'
if name == 'Alice':
    print ('Hi, Alice')
print ('Done')
'''
# Comments:
# IMPORTANT!
'''
'Alice' is a statement or a condition
if that statement or condition is True (==), DO THAT THING.
If not, DO NOTHING.
'''

# Let's Test This
'''
name = input()
if name == 'Alice':
    print ('Hello Alice')
elif name == 'Eros':
    print ('You badass motherfucker')
else:
    print ('Hello '+name)
'''

# Password example:
'''
password = input('Please type in your password: ')
if password == "swordfish":
    print ('Access Granted')
    print ('Welcome Mr. Balls of Steel.')
else:
    print ('Access Denied')
'''

# Undead Example
'''
name = 'Bob'
age = 3000
if name == 'Alice':
    print ('Hi Alice!')
elif age < 12:
    print ('You are not Alice, kid!')
elif age > 2000: # The program checks all elif statements in order
    print ('Unlike you, Alice is not an undead, immortal vampire')
elif age > 100: # order matters!
    print ('You are not Alice, grannie')
'''
