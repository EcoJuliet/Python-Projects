#REGULAR ExPRESSION SYNTAX

import re

message = 'Call me at 411-155-4563 tomorrow, or at 412-555-8985 for my office line'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # usually raw strings are passed on the re.compile()
   # we're looking for "\d digits'
print(phoneNumRegex.findall(message)) #returns a "match objects"
  
   
