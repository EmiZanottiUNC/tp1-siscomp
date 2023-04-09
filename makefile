make:
	nasm -f elf32 converter.asm
	gcc -m32 -shared -W converter.o wrapper.c -o libconvert.so

debug:
	nasm -f elf converter.asm
	gcc -g -m32 -c -o wrapper.o wrapper.c
	gcc -g -m32 converter.o wrapper.o -o wrapper

clean:
	rm *.o *.so wrapper