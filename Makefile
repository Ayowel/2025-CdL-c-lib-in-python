
IN_FILES=$(wildcard resources/code/*.c)
DUMPTOOL=nm -gD

all: presentation.html presentation-live.html
presentation: presentation.html
libs: $(subst .c,.so,$(IN_FILES))
outs: $(subst .c,.out,$(IN_FILES))
dumps: $(subst .c,.dump,$(IN_FILES))
clean:
	rm -f $(subst .c,.so,$(IN_FILES)) $(subst .c,.o,$(IN_FILES)) $(subst .c,.dump,$(IN_FILES)) $(subst .c,.out,$(IN_FILES))
purge: clean
	rm -f presentation.html presentation-live.html

.PHONY: all libs outs dumps clean purge presentation

presentation.html: presentation.adoc outs dumps
	bundle exec asciidoctor-revealjs presentation.adoc

presentation-live.html: presentation.adoc outs dumps
	bundle exec asciidoctor-revealjs presentation.adoc -a live-presentation -o presentation-live.html

%.dump: %.so
	$(DUMPTOOL) $< >$@

%.so: %.o
	$(CC) $< -shared -o $@

%.o: %.c
	$(CC) -c -Wall -Werror -fpic $< -o $@

%.out: %.py %.so
	./$< > $@
