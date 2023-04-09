#include <stdio.h>
#include <stdlib.h>

extern float asm_main(float, float) __attribute__((cdecl));

float convert(float base, float exchange) {
    return asm_main(base, exchange);
}

int main(){}