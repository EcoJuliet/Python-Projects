#!/usr/local/bin/python3
# IMPORTING DATE AND TIME
''' HEADERS ARE:
now.day
now.month
now.year
now.hour
now.minute
now.second
'''

from datetime import datetime
now = datetime.now()
# THIS IS NEEDED TO IMPORT THE DATETIME MODULE
print ('%s/%s/%s'  % (now.month, now.day, now.year)), print ('%s:%s:%s' % (now.hour, now.minute, now.second))
#PLEASE INSERT EVERYTHING IN THE PARENTHESIS ON THE PRINT FUNCTION

# Let's play a little.
# Expected result: 'Hello (NAME), you are (ACTION) at (HOUR), good for you!'
name = input('Please insert your name: ')
action = input('What are you doing right now? ')
print ('Hello,',name,', you are',action,'at','%s:%s:%s' %(now.hour, now.minute, now.second),', good for you!\n\n')


print ('ACHIEVEMENT: Being productive... maybe...')
import os
os.system('pause')
# END
