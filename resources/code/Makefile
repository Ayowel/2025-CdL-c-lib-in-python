
IN_FILES=$(wildcard *.c)
DUMPTOOL=nm -gD

all: outs dumps
libs: $(subst .c,.so,$(IN_FILES))
outs: $(subst .c,.out,$(IN_FILES))
dumps: $(subst .c,.dump,$(wildcard *_simple_*.c))
clean:
	rm -f *.so *.o *.dump *.out

.PHONY: all libs outs dumps clean

%.dump: %.so
	$(DUMPTOOL) $< >$@

%.so: %.o
	$(CC) $< -shared -o $@

%.o: %.c
	$(CC) -c -Wall -Werror -fpic $< -o $@

%.out: %.py %.so
	./$< > $@
