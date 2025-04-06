def flip_operators(expr):
    flipped = ""
    flip_map = {
        '+': '-', '-': '+',
        '*': '/', '/': '*'
    }
    for char in expr:
        flipped += flip_map[char] if char in flip_map else char
    return flipped
