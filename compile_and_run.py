import subprocess
import os

def save_and_compile_asm(asm_code, filename="output"):
    asm_file = f"{filename}.asm"
    obj_file = f"{filename}.obj"
    exe_file = f"{filename}.exe"

    # Save ASM code
    with open(asm_file, 'w') as f:
        f.write(asm_code)

    # Assemble with NASM
    subprocess.run(["nasm", "-f", "win32", asm_file, "-o", obj_file], check=True)

    # Link using GoLink (or change to gcc or another linker if needed)
    subprocess.run(["gcc", obj_file, "-o", exe_file], check=True)

    # Run the exe and capture the output
    result = subprocess.run([exe_file], capture_output=True, text=True)
    return result.stdout.strip()
