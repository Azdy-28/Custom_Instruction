temp_count = 0

def new_temp():
    global temp_count
    temp = f"t{temp_count}"
    temp_count += 1
    return temp

def generate_tac(ast):
    code = []
    def helper(node):
        if node.left is None and node.right is None:
            return node.value[1]
        left = helper(node.left)
        right = helper(node.right)
        if node.value[1] == '=':
            code.append(f"{left} = {right}")
            return left
        temp = new_temp()
        code.append(f"{temp} = {left} {node.value[1]} {right}")
        return temp
    helper(ast)
    return code