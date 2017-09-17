# Guess the number game!
import random

print ('Hello. What\'s your name?')
user_name = input()
print ('Hi,'+user_name+' let\'s play a game! ', end='')
print ('Can you guess the number I\'m thinking?')


print ('Well, I\'m thinking of a number between 1 and 20')
secretnumber = random.randint (1, 20)

for guesses_taken in range(1, 7): # starts at one, ends at 6
    print ('Take a guess! ')
    guess = int(input())
    if guess < secretnumber:
        print ('Your guess is too low!\n')
    elif guess > secretnumber:
        print ('Your guess is too high!\n')
    else:
        break # the right answer

if guess == secretnumber:
    print ('Congratulations, ' + user_name+ '! You got it right!')
    print ('You took '+str(guesses_taken)+' guesses.') 
elif guess != secretnumber:
    print ('You ran out of tries this time.')
    print ('You should try again!')
    print ('The number I was thinking was '+str(secretnumber))
   
