section .data
t0 dd 0
y dd 0
z dd 0
section .text
global start
start:
mov eax, [z]
add eax, [y]
mov [t0], eax
ret