segment .text
        global  asm_main
asm_main:
        push ebp
        mov ebp, esp ;Guardo valor original de ebp y cargo el valor de esp
        fld dword [ebp + 8] ;cargo parametro 1 en unidad de punto flotante
        fld dword [ebp + 12] ;cargo parametro 2 en unidad de punto flotante
        fmul ST1 ; ST0 = ST0 * ST1
        
        pop ebp ;restauro ebp y salgo
        ret