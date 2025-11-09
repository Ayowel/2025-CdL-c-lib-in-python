# Only matching headers as .c files will be generated in this directory later
IN_FILES=$(wildcard ./*/main.c)
DUMPTOOL=nm -gD

all: dlibs slibs outs dumps
dlibs: $(subst .c,.so,$(IN_FILES))
slibs: $(subst .c,.o,$(IN_FILES))
outs: $(subst .c,.out,$(IN_FILES))
dumps: $(subst .c,.dump,$(IN_FILES))

clean:
	rm -f */mycffilib.* $(subst .c,.so,$(IN_FILES)) $(subst .c,.o,$(IN_FILES)) $(subst .c,.dump,$(IN_FILES)) $(subst .c,.out,$(IN_FILES))

.PHONY: all dlibs slibs outs dumps clean

%.dump: %.so
	$(DUMPTOOL) $< >$@

%.so: %.c
	$(CC) $< -shared -fPIC -o $@

%.o: %.c
	$(CC) -c -Wall -Werror -fpic $< -o $@

%.out: %.py %.so %.o
	./$< > $@
