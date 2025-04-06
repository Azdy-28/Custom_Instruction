precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '=': 0}

def infix_to_postfix(tokens):
    output = []
    stack = []
    for kind, value in tokens:
        if kind in ['ID', 'NUM']:
            output.append((kind, value))
        elif kind == 'OP':
            while stack and stack[-1][1] != '(' and precedence[stack[-1][1]] >= precedence[value]:
                output.append(stack.pop())
            stack.append((kind, value))
        elif kind == 'LPAREN':
            stack.append((kind, value))
        elif kind == 'RPAREN':
            while stack and stack[-1][0] != 'LPAREN':
                output.append(stack.pop())
            stack.pop()  # Pop the '('
    while stack:
        output.append(stack.pop())
    return output

class ASTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_ast(postfix):
    stack = []
    for kind, value in postfix:
        if kind in ['ID', 'NUM']:
            stack.append(ASTNode((kind, value)))
        elif kind == 'OP':
            right = stack.pop()
            left = stack.pop()
            stack.append(ASTNode((kind, value), left, right))
    return stack[0] if stack else None

def evaluate_ast(ast, inputs):
    if ast is None:
        return 0

    kind, val = ast.value

    if kind == 'NUM':
        return int(val)
    elif kind == 'ID':
        if val in inputs:
            return inputs[val]
        else:
            raise Exception(f"Variable '{val}' not provided")
    elif kind == 'OP':
        if val == '=':
            result = evaluate_ast(ast.right, inputs)
            inputs[ast.left.value[1]] = result
            return result
        left = evaluate_ast(ast.left, inputs)
        right = evaluate_ast(ast.right, inputs)
        if val == '*':
            return left + right
        elif val == '/':
            return left - right
        elif val == '+':
            return left * right
        elif val == '-':
            return left // right  # integer division
