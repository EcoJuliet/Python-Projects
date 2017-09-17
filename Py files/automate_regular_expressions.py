# REGULAR EXPRESSIONS (REGEX)

'''
regular expressions are 'mini-languages' for specifying text patterns.
Writing code to do a pattern matching without regular expressions is a huge pain (YES!)

REGEX strings often use \ backlashes (like \d), so they are often raw strings: r'\d'

- import the 're module' first
- call the re.compile() function to create a regex object.
- call the regex object's seach() method to create a match object.
- cal the match object's group() method to get the matched string.
- \d is the regex for a numeric digit character.
'''

#EXAMPLE:

import re

message = 'Call me at 411-155-4563 tomorrow, or at 412-555-8985 for my office line'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # usually raw strings are passed on the re.compile()
   # we're looking for "\d digits'
print(phoneNumRegex.findall(message)) #returns a "match objects"
  
   
# ---------------------

#Lesson 24:

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search ('My number is 456-555-1234')
mo.group()

'''
In case we want a part of an area code, 'like '456', we can use parentheses so
make groups. Like this:
'''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo.group() or m.group(0) = '456-555-1234'
mo.group(1) == '456'
mo.group(2) == '555-1234'

SE QUISER PROCURAR UM PARENTESES, TENHO QUE USAR '\(' e '\)' no re.compile!!

O Pipe Character (|) (retinho) can be used to match one of many groups.
Like: Bat(man|code|girl|mobile)


# ------------------

#Lesson 25: Repetition in Regex Patterns and Greedy/Nongreedy Matching

? -> symbol for "0 or 1".
# EXAMPLE:
batRegex = re.compile('Batman | Batwoman') == re.compile('Bat(wo)?man')
# like said, the (wo)? means it can appear 0 or 1 times in Batman


* -> zero or more times
re.compile('Bat(wo)*man')

Pode dar match em "batwowowowowowoman"

+ 1 -> ONE or more times

{x} -> exactly that amount of times.
haRegex = re.compile(r'(Ha){3}')
haRegex.search ('Oh deat Batman, HaHaHa') == True

{x,y} -> minimum and maximum numbers of repetitions

#GREEDY MATCHES:
    Vamos supor que queremos fazer uma busca {0,5}.
    Se o Python reconhecer que teve mais de um match, que abrange todos os resultados,
    ele vai me dar o maior resultado.
    Por exemplo:
digitRegex = re.compile (r'(\d){3,5}')
digitRegex.search('12345')
Resultado:
    match: 12345.
Mesmo que so o 123 já preencha os requisitos.

#Para um NON-GREEDY MATCH:
eu teria que fazer: {3,5}? - NESSE CASO, NÂO INDICA '0 ou 1', e sim "NON_GREEDY MATCH


# -------------------------------


#LESSON 26

.search() -> returns match objetcs
.findall() -> finds a list if doesn't have a group. Behavior for regex objects
that has zero or one objects.

IF it has zero or one groups: LIST OF STRINGS
+1 GROUPS: returns a list of tuples with strings inside.


# LESSON 26

# CHARACTER CLASSES

\d -> any digits
\D -> any character that IS NOT a numeric digits (everything else)
\w -> 'word' character
\W -> any character that is NOT a letter, numeric digit or the underscore
\s -> any space, tab or newline character. (matches 'space characters')
\S -> any character that is NOT a space, tba or newline.

Examples:
>>> lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'
# saving a little song a 'lyrics' variable.
>>>xmasRegex = re.compile(r'\d+\s\w+')
# the goal here is to find ONE OR MORE DIGIT, A SPACE, and ONE OR MORE WORD
#CHARACTER.
>>> xmasRegex.findall(lyrics):
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 golden', '4 calling', '3 french', '2 turtle', '1 partridge']

# ___________________


CREATE YOUR OWN CHARACTER CLASSES
ObjRegex = re.compile(r'[]')# colocar a nova classe entre os brackets
Exemplo:
vowelsRegex = re.compile(r'[aeiou]') # somente vogais
vowelsRegex = re.compile(r'[aeiouAEIOU') # somente vogais minusculos e maiusculos
alphabetRegex = re.compile(r'a-z') # todo o alfabeto minúsculo
alpha2Regex = re.compile(r'a-f') # de a até f minusculo
alpha3Regex = re.compile(r'a-fA-f') # de a até f minusculo e MAIUSCULO

NEGATIVE CHARACTER CLASSES:

    
# para inverter a classe ('o que não quero') só adicionar ^ (caret) depois do
#bracket
vowelsRegex = re.compile(r'[^aeiou]')
vowelsRegex = re.compile(r'[^aeiouAEIOU') 
alphabetRegex = re.compile(r'[^a-z]') 
alpha2Regex = re.compile(r'[^a-f]') 
alpha3Regex = re.compile(r'[^a-fA-f]')    

"FAÇA O OPOSTO"


EXEMPLO:
    consonantsRegex.findall(r'[^aeiouAEIOU]')



# ---------------------
# LESSON 27



CHARACTER CLASSES - continuação.
SPECIAL CHARACTERS:
^
Regex = re.compile(r'^qqcoisaaqui') - o ^ no começo, indica que
                                            o que estou procurando tem que
$                                            aparecer no começo da string!
Regex = re.compile(r'qqcoisaqui$') - o $ no finao, indica que o que estou
                                            procurando tem que aparecer no
^$                                            começo da string!
Regex = re.compile(r'^qqcoisaqui$') - com os dois, a STRING TEM QUE SER EXATA

. (pãoto) - tipo coringa. fora novalinha
Regex = re.compile(r'^.qqcoisaaqui') - 'qq coisa que termina em ''qqcoisaaqui'.                                           

.* - dot-star combo. - qualquer coisa em qualquer forma.
#                                           
Versão NON-GREEDY: .*?
                                            
Regex = re.compile(r'.*')
>>> 'First Name: Eros Last Name: Junior'
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')                                            
>>> nameRegex.findall('First Name: Eros Last Name: Junior')
[('Eros', 'Junior')] - achou meu nome dentro de uma tuple (parenteses)

o . acha tudo com EXCEÇÃO do newline (novalinha)


para tirar essa exceção:

#####    
re.compile(r'.*', re.DOTALL) - adicionar o argumento re.DOTALL depois da vírgula
re.compile(r'aeiou', re.INGORECASE) - aceita AEIOU e aeiou.
#####

# ------------------------------- 

# LESSON 28: The sub() Method and Verbose Mode.

"Find and replace"

.sub('TEXTO SUBSTITUTO', 'STRING TO TEXTO A SER SUBSTITUIDO' ) Method - 'find and substitute.

DEPOIS DE COMPILAR (re.compile) O QUE QUERO QUE O REGEX ACHE,
eu posso SUBSTITUIR o texto por algo que eu queira.
FORMATO

>>> import re
>>> namesRegex = re.compile(r'Agent \w+') # Agent qualquer nome.
>>> namesRegex.findall('Agent Alice gave the secret documents to Agent Bob')
['Agent Alice', 'Agent Bob'] # resultados do findall
>>> namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob') # comando sub()
'REDACTED gave the secret documents to REDACTED' #resultado

PARA FAZER SUBSTITUIÇÕES

>>> namesRegex = re.compile(r'Agent (\w)\w*') # primeiro grupo é uma letra só.
>>> namesRegex.findall('Agent Alice gave the secret documents to Agent Bob')
['A', 'B'] # vista aqui.
>>> namesRegex.sub(r'Agent \1****','Agent Alice gave the secret documents to Agent Bob') # raw!!
# uso o primeiro grupo (letra) para entrar no texto que sera trocado.
# o que o \NUMERO diz é 'quero uma parte da string original na string nova, pelo grupo TAL.
'Agent A**** gave the secret documents to Agent B****' # resultado

# ---------------------

VERBOSE MODE

O modo VERBOSE faz com que o Python e o Regex nao reconheçam linhas e espaços em branco
dentro da string do RE.COMPILE()
Exemplo:

re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # pode ficar muito confuso.
# COM VERBOSE , USAR O TRIPLE QUOTES PARA FAZER NOVAS LINHAS.
re.compile(r'''
(\d\d\d-)|      # posso comentar. AREA CODE, PRIMEIRO GRUPO. COM DASH
(\(\d\d\d\))    # da hora né?. -or- AREA CODE COM PAREN, SEM DASH.
\d\d\d          # first 3 digits.
-               # second dash
\d\d\d\d        # last 4 digits
\sx\d{2,4}      # extension, likex1234''', re.VERBOSE)


LEMBRETE PARA OS ARGUMENTOS:
    re.compile(r'TEXTO', re.IGNORECASE) #ignora maiusulas e minucsculas
    re.compile(r'TEXTO', re.DOTALL) #o 'dot' aceita tudo fora NEWLINE
    re.compile(r'TEXTO', re.VERBOSE) # verbose para poder comentar e adicionar linhas

PARA USAR MAIS DE UM AO MESMO TEMPO:
    re.compile(r'TEXTO', re.VERBOSE | re.DOTALL | re.IGNORECASE) # usar o |



# ------------------

# LESSON 29: PHONE AND E-MAIL SCRAPER











