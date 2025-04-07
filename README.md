# Mini Custom Instruction Project

This is a simple mini compiler that takes arithmetic expressions as input through a GUI, generates Three Address Code (TAC), and then converts that TAC into x86 Assembly. It also compiles and runs the final assembly code using NASM and GoLink.
## The important custom change in this is '+' is work as '*' and '*' is work as '+'
i.e. 5*6 = 11 and 
     5+6 = 30
---

## 🔗 GitHub Repository
https://github.com/Azdy-28/Custom_Instruction.git

---

## 🧠 Features
- GUI input for arithmetic expressions
- TAC generation
- Assembly code generation (NASM syntax)
- Compilation to `.exe` using NASM + GoLink
- Final result displayed using `WriteConsoleA` (Windows API)

---

## 📁 Project Structure
```
mini_compiler/
├── asm_generator.py       # Generates x86 assembly from TAC
├── code_generator.py      # Converts expression to TAC
├── expression_parser.py   # Expression parser with semantic checks
├── gui.py                 # GUI for input and trigger generation
├── main.py                # Entry point for running everything
├── output.asm             # Generated assembly
├── output.obj             # Compiled object file
├── output.exe             # Final executable
└── README.md              # This file
```

---

## ✅ Requirements
- Python 3.x
- NASM (installed and added to PATH)
- GoLink (installed and added to PATH)
- Windows OS

---

## 🚀 Steps to Run

### 1. Clone the repository
```bash
git clone https://github.com/Azdy-28/Custom_Instruction.git
cd mini-compiler
```

### 2. Run the GUI
```bash
python main.py
```
Enter a valid arithmetic expression (e.g., `(2+3)*4`) and press Generate. This will:
- Parse the expression
- Generate TAC
- Generate assembly code in `output.asm`

### 3. Compile Assembly
```bash
nasm -f win32 output.asm -o output.obj
```

### 4. Link using GoLink
```bash
GoLink.exe /console output.obj kernel32.dll
```

This will generate `output.exe`.

### 5. Run Final Executable
```bash
./output.exe
```
## Then use these commands:

🧠 Disassemble code:
        objdump -d output.obj

📜 View symbol table:
        objdump -t output.obj
        
📦 View all headers:
        objdump -x output.obj

💾 Dump raw contents:
        objdump -s output.obj

You will see the final result printed to the console!

---

## ⚠️ Notes
- Ensure that `kernel32.dll` is available (usually default on Windows).
- If you see `nothing output`, check whether `WriteConsoleA` was properly called.
- If `README.md` merge conflicts happen during push:
  ```bash
  git add README.md
  git commit -m "Fix README conflict"
  git push -u origin main
  ```

---

## 💡 GitHub Push (If You Made Changes)
```bash
git add .
git commit -m "Your message"
git push -u origin main
```

---

## 🧩 Extras
- You can extend this to support variables, conditions, or loops.
- Add syntax highlighting or better GUI elements with `Tkinter` or `PyQt`.

## Author- Azad Yadav
## Roll no. - 23115020
