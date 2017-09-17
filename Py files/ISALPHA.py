# PygLatin Translation version 1.0
pyg = 'ay'
# This created the "ay" index.
original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print (original)
# This is to test if the person actually typed something that's not a numeral in the field.
else:
    print ('Please type in a word, would ya?')
#Now to the coding:    
word = original.lower() # make it lowecase
first = word[0] #"original" is in here now
new_word = word+first+pyg
new_word = new_word[1:len(new_word)]
# this changed the "word+first+pyg" to the new deal.
print (new_word)
