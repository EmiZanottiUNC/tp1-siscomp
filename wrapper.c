#include <stdio.h>
#include <stdlib.h>

float asm_main(float, float) __attribute__((cdecl));

int main() {
    float ret_status = 0;
    ret_status = asm_main(4.3, 2.1);
    printf("%f\n",ret_status);
}