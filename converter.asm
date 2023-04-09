segment .text
        global  asm_main
asm_main:
        push ebp
        mov ebp, esp
        fld dword [ebp + 8]
        fld dword [ebp + 12]
        fmul ST1
        
        sub esp, 4
        fstp dword [esp]
        mov eax, dword [esp]
        add esp, 4
        
        mov esp, ebp
        pop ebp
        ret