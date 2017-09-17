# STRING METHODS

DICAS:

X.upper() - troca todas as letras de uma string para maiúsculas
X.lower() - troca todas as letras de uma string para minusculas.


importante por quê?

Porque 'YES' != 'yes' no Python, MAS
spam = 'YES'
spam.lower() == 'yes' == True

# --------------------

X.isupper()
x.islower()
x.title() - 'hellow world' = 'Hello World"
Retorna um boolean (true/false) se a string é em maisucula ou nao.

# --------------------

Dá pra encadear isso:
'hello'.upper().isupper = True

# --------------------

'hello'.isalpha() - letters only
'hello123'.isalnum() - letters and numbers only
'123'.isdecimal() - numbers only
'   '.isspace() - whitespace only
'Hello'.istitle() - titlecast only # return 'true' if all words begin with uppercase word
.startswith()
.endswith()
.join() - returns a string that combines strings FROM A LIST
exemplo:
    ','.join(['cats', 'rats', 'bats']) == 'cats,rats,bats'
    'AAA'.join(['cats', 'rats', 'bats']) =='catsAAAratsAAAbats'
.split() - eu digito uma string, e ele retorna uma lista. O separador esta dentro do  () 
exemplo:
    >>> 'Olá, meu nome e Eros'.split('e')
    ['Olá, m', 'u nom', ' ', ' Eros']
    >>> 'olá meu nome e eros'.split()
    ['olá', 'meu', 'nome', 'e', 'eros']

.ljust(X) - justifica um texto, "X" representa o tamanho total que quero que tenha
.rjust(X) -
exemplo:
    >>> 'ABERLARDO'.rjust(20)
    '           ABERLARDO'
    >>> len('ABELARDO'.rjust(20))
    20
    >>> 'ABSTRUDEL'.rjust(20, "-") # da pra escolher.
    '-----------ABSTRUDEL'
    
.center(X) - centra um texto
.strip() - quando a gente quer tirar algo da string, NOS EXTREMOS
.rstrip() - TIRA DO EXTREMO DIREITO
.lstrip() - TIRA DO EXTREMO ESQUERDO
.replace(dois, argumentos) - primeiro o que sai, depois o que entra.
exemplo:
    >>> spam = 'A ALMONDEGA MATA MUITO DE DOR'
    >>> spam.replace('a'.upper(),'e'.upper() )
    'E ELMONDEGE METE MUITO DE DOR'

.find() - acha o que tá nos parenteses


DA PRA FAZER A ZOEIRA, por exemplo:
'Hello world"[5].isspace() == 'true'    

