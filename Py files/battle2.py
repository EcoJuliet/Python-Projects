# Battle Rules
num_knights = int(input('How many knights are there? '))
day = input('What day is Today? ')
enemy = input('Enter type of enemy: ')

if enemy == 'Killer Bunny':
    print ('Holy Hand Grenade!')
else:
    # Original Battle Rules
    if num_knights < 3 or day == 'Monday':
        print ('RUN FOR YOUR LIVES!')
    elif num_knights >= 10 and day == 'Wednesday':
        print ('TROJAN RABBIT!')
    else:
        print ('Truce?')
# End of Code

