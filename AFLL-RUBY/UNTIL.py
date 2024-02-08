from ply import lex, yacc
tokens = ( 'IDENTIFIER', 'NUMBER', 'EQUALS', 'LPAREN', 'RPAREN','PUTS','STRING','WHILE','END','PLUS','EQUALS_TO','UNTIL','DO')

def t_WHILE(t):
    r'while'
    return t

def t_END(t):
    r'end'
    return t

def t_PUTS(t):
    r'puts'
    return t

def t_EQUALS(t):
    r'=='
    return t

def t_UNTIL(t):
    r'until'
    return t

def t_DO(t):
    r'do'
    return t

def t_EQUALS_TO(t):
    r'='
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_STRING(t):
    r"'[^']*'"
    t.value = t.value[1:-1]  # Remove the quotes
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_statement_while(p):
    'statement : WHILE expression statements END'
    print("While statement:", p[2])

def p_statement_until(p):
    'statement : UNTIL expression DO statements END'
    print("Until statement:", p[2])

def p_statements(p):    #Parses a list of statements.

    '''statements : statement statements
                  | statement
                  | empty'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f'{p[1]}\n{p[2]}'

def p_expression(p):
    '''expression : expression PLUS expression
                  | IDENTIFIER
                  | NUMBER
                  | LPAREN expression RPAREN
                  | expression EQUALS expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
    '''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = ('add', p[1], p[3])
        elif p[2] == '-':
            p[0] = ('subtract', p[1], p[3])
        elif p[2] == '*':
            p[0] = ('multiply', p[1], p[3])
        elif p[2] == '/':
            p[0] = ('divide', p[1], p[3])
        elif p[2] == '==':
            p[0] = ('equality', p[1], p[3])
    else:
            p[0] = p[1]

def p_statement(p): 
    '''statement : PUTS STRING
                 | IDENTIFIER EQUALS_TO expression'''
    
    # Define the action for the expression
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
                

def p_error(p):
    print(f"Syntax error at '{p.value}'")
    parser.success = False

def p_empty(p):  #This is an empty parsing rule. It doesn't do anything. It's used in the parser to represent an empty production if needed.
    'empty :'
    pass

parser = yacc.yacc()

# Testing
input_string = "until x==2 do x=a+b end"
parser.success = True  
result = parser.parse(input_string)

if parser.success:
    print("Successful parsing")
else:
    print("Invalid input")