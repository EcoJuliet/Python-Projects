# Is PhoneNumber
def isPhoneNumber(text): # 415-555-1234
    if len(text) != 12: # see if its the north-american lengh system
        return False #not phone number-sizes
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # Missing first dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False #no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True

print (isPhoneNumber('415-555-1234'))

message = 'Call me at 413-555-1334 tomorrow, or at 412-555-4311 for my office line'
foundNumber = False # because it hasn't found a number yet
for i in range(len(message)):
    chunk = message[i:i+12] #test every 12 caracters in 'message' for
    if isPhoneNumber(chunk): #calls isPhoneNumber function to see if it's True!
        print ('Phone Number found: '+ chunk)
        foundNumber = True
if not foundNumber:
    print ('Could not find any phone numbers')

## ALL THIS CAN BE REPLACES WITH THE RE MODULE
