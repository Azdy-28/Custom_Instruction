def generate_assembly(tac):
    asm = []
    data_section = ["section .data"]
    text_section = ["section .text", "global start", "start:"]

    variables = set()
    for instr in tac:
        parts = instr.split()
        if len(parts) == 3 and parts[1] == '=':
            src = parts[2]
            if src.isdigit():
                text_section.append(f"mov eax, {src}")
            else:
                text_section.append(f"mov eax, [{src}]")
                variables.add(src)
            text_section.append(f"mov [{parts[0]}], eax")
            variables.add(parts[0])

        elif len(parts) == 5:
            dest, _, left, op, right = parts
            text_section.append(f"mov eax, [{left}]")
            variables.update([dest, left, right])

            asm_op = {'+': 'add', '-': 'sub', '*': 'imul', '/': 'idiv'}[op]
            if asm_op == 'idiv':
                text_section.append("cdq")
                text_section.append(f"idiv dword [{right}]")
            elif asm_op == 'imul':
                text_section.append(f"imul eax, [{right}]")
            else:
                text_section.append(f"{asm_op} eax, [{right}]")

            text_section.append(f"mov [{dest}], eax")

    # Declare all variables in .data section
    for var in sorted(variables):
        data_section.append(f"{var} dd 0")

    # Exit
    text_section.append("ret")

    asm = data_section + text_section
    return asm

def save_asm_to_file(asm, filename="output.asm"):
    cleaned_asm = [line.strip() for line in asm if line.strip() != ""]
    with open(filename, "w", newline="\n") as f:
        f.write("\n".join(cleaned_asm))

