from ply import lex, yacc

tokens = ('FOR', 'VAR', 'INT', 'IN','STRING', 'PUTS', 'END','DOT')

t_ignore=' \t'

def t_PUTS(t):
    r'(\s)*puts'
    return t

def t_DOT(t):
    r'\..'
    return t

def t_IN(t):
    r'(\s)*in'
    return t

def t_FOR(t):
    r'(\s)*for'
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"(?:\\.|[^"])*"'
    t.value = t.value[1:-1]  
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_END(t):
    r'(\s)*end'
    return t

def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)
   
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def p_start(p):
    'start : for_block END'
    p[0] = "Valid Ruby for loop"

def p_for_block(p):
    'for_block : FOR VAR IN  INT DOT INT statements'
    p[0] = "Valid Ruby for loop"

def p_statements(p):
    'statements : PUTS STRING '
    
def p_error(p):
    if p:
         print(f"Syntax error at '{p.value}'")
    else:
         print(f"Invalid Syntax")
         
lexer = lex.lex()
parser = yacc.yacc()

def check_for_loop_syntax(input_text):
    result = parser.parse(input_text, lexer=lexer)
    return result

input_text = """
for a in 1.10
    puts "this works!"

"""

result = check_for_loop_syntax(input_text)
print(result)

'''VALID : for i in 1..5
    		puts "for loop"
	   end
	   for a in 1..10
    		puts "this works!"
	   end
   INVALID:for i in 1.5
    		puts "for loop"
	   end
           for i in 1..5:
  	        puts "for loop"
	   end
'''




