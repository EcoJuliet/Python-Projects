# This program says 'hello' and asks for my name.

print ('Hello world'+'!'*3)

print ('What is your name? ') # ask for they name.
my_name = input()
print ('It is good to meet you, ' + my_name)
print ('The length of your name is: ')
print (len(my_name))

print ('What is your age? ') # asks your age.
my_age = input() # input ALWAYS returns a STRING value!
print ('You are '+str(int(my_age))+' years old') # change to int for numbers!
print ('You will be ' + str(int(my_age)+ 1) + ' in a year')
print ('Thank you and I\'ll see you next time!')
