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
