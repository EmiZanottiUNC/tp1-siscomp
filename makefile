make:
	nasm -f elf converter.asm
	gcc -m32 -c -o wrapper.o wrapper.c
	gcc -m32  converter.o wrapper.o -o wrapper

debug:
	nasm -f elf converter.asm
	gcc -g -m32 -c -o wrapper.o wrapper.c
	gcc -g -m32 converter.o wrapper.o -o wrapper

clean:
	rm *.o wrapper