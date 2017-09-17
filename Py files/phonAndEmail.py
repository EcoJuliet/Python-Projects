#! python3

import re, pyperclip

# Create a regex for phone numbers

phoneRegex = re.compile(r'''
# examples: 415-555-0000, 555-0000, (415) 555-0000, 555-000 ext 12345, ext., x12345
(                           # group zero 0
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional) sem ou COM parens
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|x)           # extension part (optional)
  (\d{2,5}))?               # extension part 2
  )
''', re.VERBOSE)

# TODO: Create a regex for email adresses
# has no groups, is sexy and working all right.
emailRegex = re.compile(r'''
                            # example: something.+_@(\d{2,5}))?.com

[a-zA-Z0-9_.+-]+            # name part. CREATE OUR OWN CHARACTER CLASS. ONE OR MORE
@                           # @ symbol
[a-zA-Z0-9_.+-]+            # domain name part

''', re.VERBOSE)
# TODO: Get the text off the clipboard
text = pyperclip.paste()

'''DEBUG'''
text = '''555-423-1234', 'carvalho.eros@gmail.com', '456-456-7894', 'jhonn@gat_col.com'''
'''DEBUG'''

# TODO: Extract the email and phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = [] # creating a blank list to put all phone Numbers into
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0]) # when the loop completes, the allPhoneNumbers list will have the first string
                                          # from the tuple that extractedPhone gerenates


'''
print ('DEBUG:')
print (extractedPhone)
print ('DEBUG:')
print (allPhoneNumbers)
print (extractedEmail)
'''
# TODO: Copy the extracted e-mail and phone to the clipboard.

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results) # joga o texto no clipboard!
print (results) # não é obrigatório.
