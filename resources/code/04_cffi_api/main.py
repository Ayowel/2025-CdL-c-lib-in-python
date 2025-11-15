#!/usr/bin/env python

from cffi import FFI
import os

# Required to use relative sources paths
os.chdir(os.path.dirname(__file__))

# tag::cffi_compile[]
ffi = FFI()
ffi.cdef("float addme(float a, float b);")
ffi.set_source("mycffilib",'#include "main.h"',sources=["main.c"])
ffi.compile()
# end::cffi_compile[]

print("# tag::cffi_use[]")
# tag::cffi_use[]
from mycffilib import lib as mycffi
print(mycffi.addme(2.3, 3.6))
# end::cffi_use[]
print("# end::cffi_use[]")
