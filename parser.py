import ply.yacc as yacc
from lexer import tokens

_last_error = None  # private error message variable

def p_statement_assign(p):
    'statement : ID EQUALS expression'
    p[0] = ('=', p[1], p[3])

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_error(p):
    global _last_error
    if p:
        _last_error = f"Syntax error at '{p.value}'"
    else:
        _last_error = "Syntax error at EOF"

parser = yacc.yacc()

def parse_with_error(data):
    global _last_error
    _last_error = None
    result = parser.parse(data)
    return result, _last_error
