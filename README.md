# Use C libs in Python

This is the support for a presentation given at Capitole du Libre in 2025.

See the presentation at https://ayowel.github.io/2025-CdL-c-lib-in-python/ .

## Build the presentation

To build the presentation, make sure that you have the following applications installed and in your `PATH`:

* [Ruby 3+](https://www.ruby-lang.org/en/) with [Bundle](https://rubygems.org/gems/bundler/)
* [Make](https://www.gnu.org/software/make/)
* A [GCC](https://gcc.gnu.org/)-like compiler and the `nm` [binutil](https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git)

Once all binaries are installed:

* Install Gem dependencies with `bundle install`
* Build the presentation with `make presentation`

## Go offline

To use the presentation offline, run kroki and revealjs servers locally and have the presentation point to it (you should execute the `compose` once while online to pull and generate container images before going offline):

```sh
cd compose
podman compose up -d
ASCIIDOC_OPTS='-a kroki-server-url=http://127.0.0.1:8000 -a revealjsdir=http://127.0.0.1:8001' make presentation
```
