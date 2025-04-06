# compiler.py
from lexer import tokenize
from parser import infix_to_postfix, build_ast, evaluate_ast, generate_3ac, generate_assembly

inputs = {}  # 🔥 Global, persistent variable storage

def compile_expression(expr):
    global inputs
    tokens = tokenize(expr)
    postfix = infix_to_postfix(tokens)
    ast = build_ast(postfix)
    tac = generate_3ac(ast)
    asm = generate_assembly(tac)
    result = evaluate_ast(ast, inputs)  # 🔄 Keep values of x, y etc
    return tokens, postfix, tac, asm, result, ast, inputs  # 🔁 return inputs too
