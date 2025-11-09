
CODEDIR=resources/code
ASC_OPTS=${ASCIIDOC_OPTS}

all: presentation presentation-live.html
presentation: presentation.html

code:
	make -C $(CODEDIR) all
clean:
	make -C $(CODEDIR) clean
purge: clean
	rm -f presentation.html presentation-live.html

.PHONY: all code clean purge presentation

presentation.html: presentation.adoc code
	bundle exec asciidoctor-revealjs -r asciidoctor-kroki ${ASC_OPTS} presentation.adoc

presentation-live.html: presentation.adoc code
	bundle exec asciidoctor-revealjs -r asciidoctor-kroki ${ASC_OPTS} presentation.adoc -a live-presentation -o presentation-live.html
