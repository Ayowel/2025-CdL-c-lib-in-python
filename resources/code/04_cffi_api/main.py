#!/usr/bin/env python

from cffi import FFI
import os

# Required to use relative sources paths
os.chdir(os.path.dirname(__file__))

# tag::cffi_compile[]
builder = FFI()
builder.cdef("float addme(float a, float b);")
builder.set_source("mycffilib",'#include "main.h"',sources=["main.c"])
builder.compile()
# end::cffi_compile[]

# tag::cffi_use[]
from mycffilib import lib as mycffi
print(mycffi.addme(2.3,3.6))
# end::cffi_use[]
