symbol_table = set()

def semantic_check(ast):
    if not ast:
        return
    kind, val = ast.value
    if kind == 'OP' and val == '=':
        if ast.left.value[0] != 'ID':
            raise Exception("Left-hand side of assignment must be an identifier")
        symbol_table.add(ast.left.value[1])
    else:
        for node in [ast.left, ast.right]:
            if node:
                semantic_check(node)