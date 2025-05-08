# Parsing & Intermediate representations: Bottom up parsing- LR parser, yacc,three address
# code generation, syntax directed translation, translation of types, control statements 

pip install ply

import ply.lex as lex
import ply.yacc as yacc

# ---------------------------------------------------
# 1. Lexical Analyzer
# ---------------------------------------------------

tokens = (
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'ASSIGN', 'LPAREN', 'RPAREN',
    'SEMI', 'IF', 'ELSE', 'INT',
    'LT', 'GT', 'EQ'
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMI    = r';'
t_LT      = r'<'
t_GT      = r'>'
t_EQ      = r'=='

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT'
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\r'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# ---------------------------------------------------
# 2. Parser + Intermediate Code Generation
# ---------------------------------------------------

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

symbol_table = {}
tac = []  # Three-address code
temp_count = 0

def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"

# Grammar rules
def p_program(p):
    '''program : statements'''
    print("\n✅ Parsing Successful")
    print("\nSymbol Table:", symbol_table)
    print("\nThree Address Code:")
    for code in tac:
        print(code)

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    pass

def p_statement_decl(p):
    'statement : INT ID SEMI'
    symbol_table[p[2]] = 'int'

def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMI'
    tac.append(f"{p[1]} = {p[3]}")

def p_statement_if(p):
    'statement : IF LPAREN condition RPAREN statement'
    label = new_temp()
    tac.append(f"if not {p[3]} goto {label}")
    tac.append(f"# if body")  # simulate nested body
    tac.append(f"{label}:")

def p_condition(p):
    '''condition : expression LT expression
                 | expression GT expression
                 | expression EQ expression'''
    temp = new_temp()
    tac.append(f"{temp} = {p[1]} {p[2]} {p[3]}")
    p[0] = temp

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    temp = new_temp()
    tac.append(f"{temp} = {p[1]} {p[2]} {p[3]}")
    p[0] = temp

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = str(p[1])

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at token: {p.type} -> {p.value}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

# ---------------------------------------------------
# 3. Input Example (Includes if, types, TAC generation)
# ---------------------------------------------------

input_code = """
int x;
int y;
x = 5;
y = x + 2 * 3;
if (x < y)
    x = y;
"""

print("Source Code:\n", input_code)
parser.parse(input_code)

