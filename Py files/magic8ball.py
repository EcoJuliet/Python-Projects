# Magic 8ball.

import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'I believe it is'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Try again'
    elif answer_number == 5:
        return 'Please, try again later'
    elif answer_number == 6:
        return 'I would say, no'
    elif answer_number == 7:
        return 'Not really'
    elif answer_number == 8:
        return 'Absolutely not'
    elif answer_number == 10:
        return 'Jesus fucking no'

print ('Think of a yes/no question and press enter to see the result.')
input ()

print (get_answer(random.randint(1,9)))
