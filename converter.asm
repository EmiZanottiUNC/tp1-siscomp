segment .text
        global  asm_main
asm_main:
        push ebp
        mov ebp, esp
        fld dword [ebp + 8]
        fld dword [ebp + 12]
        fmul ST1
        
        mov esp, ebp
        pop ebp
        ret