from ply import lex, yacc
tokens = ( 'IDENTIFIER', 'NUMBER','STRING','EQUALS_TO','COMMA','OPEN_BRACKET','CLOSE_BRACKET')

def t_EQUALS_TO(t):
    r'='
    return t

def t_STRING(t):
    r'(\'[^\']*\'|\"[^\"]*\")'
    t.value = t.value[1:-1]  # Remove the quotes
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_COMMA = r','
t_OPEN_BRACKET = r'\['
t_CLOSE_BRACKET = r'\]'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser

def p_array_declaration(p):
    'statement : IDENTIFIER EQUALS_TO OPEN_BRACKET array_elements CLOSE_BRACKET'

def p_array_elements(p):
    '''array_elements : array_value COMMA array_elements
                      | array_value
                      | empty'''


def p_array_value(p):
    '''array_value : NUMBER
                   | STRING
                   | IDENTIFIER'''


def p_error(p):
    print(f"Syntax error at '{p.value}'")
    parser.success = False

def p_empty(p):  #This is an empty parsing rule. It doesn't do anything. It's used in the parser to represent an empty production if needed.
    'empty :'
    pass

parser = yacc.yacc()

# Test the parser
input_string = 'a={1,2,3]'
parser.success = True  # Initialize success flag
result = parser.parse(input_string)

if parser.success:
    print("Successful parsing")
else:
    print("Invalid input")


'''INVALID:a==[1,2,"abc",8],a[1,2,"abc",8],a={1,2,"abc",8]
   VALID  :a=[1,2,"abc",3,4],a=[]'''

