#while function
# It runs the function WHILE it's true. As soons as it's false. it stops.

'''
spam = 0
while spam < 5:
    print ('Hello world')
    spam = spam+1 # prints 'Hello world" 5 times and stops because it ITERATES 5 times.
'''

# While example 2:
'''
name = '' # Empty brackets returns "False" always
while name != 'your name':
    print ('Please type your name: ')
    name= input()
print ('Thank you')
'''

# Example 3:
'''
spam = 0
while spam < 10:
    spam = spam + 1
    if spam == 3:
        print ('Spam now equals to '+str(spam))
        continue # KEEP IT GOING!
    print ('Spam is '+str(spam))
'''
'''
RESULT:
Spam is 1
Spam is 2
Spam is now equals to 3
Spam is 4
Spam is 5
Spam is 6
Spam is 7
Spam is 8
Spam is 9
Spam is 10'''


