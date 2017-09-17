# Cats program.

print ('How many cats do you have?')

num_cats = input()
try:
    if int(num_cats) < 0:
        print ('Please type in a positive number.')
    elif int(num_cats) == 0:
        print ('You should get a cat!')
    elif int(num_cats) >= 4:
        print ('That\'s a lot of cats')
    else:
        print ('That aren\'t that many cats')
except:
    print ('You didn\'t enter a number.')
