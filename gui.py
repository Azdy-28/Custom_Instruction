from tkinter import simpledialog
import tkinter as tk
from parser import evaluate_ast
from lexer import tokenize
from parser import infix_to_postfix, build_ast
from semantic import semantic_check
from tac_generator import generate_tac
from asm_generator import generate_assembly, save_asm_to_file

def compile_expression(expr):
    tokens = tokenize(expr)
    postfix = infix_to_postfix(tokens)
    ast = build_ast(postfix)
    semantic_check(ast)
    tac = generate_tac(ast)
    asm = generate_assembly(tac)
    save_asm_to_file(asm)  # Save assembly to output.asm

    variables = {val for kind, val in tokens if kind == 'ID'}
    inputs = {}
    for var in variables:
        val = simpledialog.askstring("Input", f"Enter value for {var}:")
        try:
            inputs[var] = int(val)
        except:
            raise Exception(f"Invalid input for variable {var}")

    result = evaluate_ast(ast, inputs)

    return tokens, postfix, tac, asm, result

def run_gui():
    def on_compile():
        expr = input_entry.get()
        try:
            tokens, postfix, tac, asm, result = compile_expression(expr)
            output_text.delete('1.0', tk.END)
            output_text.insert(tk.END, f"Tokens: {tokens}\n")
            output_text.insert(tk.END, f"Postfix: {postfix}\n")
            output_text.insert(tk.END, f"3AC:\n" + "\n".join(tac) + "\n")
            output_text.insert(tk.END, f"Assembly:\n" + "\n".join(asm) + "\n")
            output_text.insert(tk.END, f"Assembly saved to output.asm ✅\n")
            output_text.insert(tk.END, f"Final Result: {result}")
        except Exception as e:
            output_text.delete('1.0', tk.END)
            output_text.insert(tk.END, f"Error: {e}")

    root = tk.Tk()
    root.title("AZAD YADAV'S Mini Compiler")

    input_entry = tk.Entry(root, width=50)
    input_entry.pack(pady=10)

    compile_button = tk.Button(root, text="Compile", command=on_compile)
    compile_button.pack(pady=5)

    output_text = tk.Text(root, height=20, width=60)
    output_text.pack(pady=10)

    root.mainloop()
