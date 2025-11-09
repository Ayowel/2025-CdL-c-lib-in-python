#!/usr/bin/env python
import os
import sys

dll_path = f"{os.path.splitext(__file__)[0]}.so"

def tprint(tag, text):
    print(f"tag::{tag}[]\n{text}\nend::{tag}[]")

# tag::cffi_build[]
import cffi
ffi = cffi.FFI()
ffi.cdef('''
    void hello();
    extern int version;
    ''')
dll = ffi.dlopen(dll_path)
# end::cffi_build[]

print("tag::cffi_run[]")
sys.stdout.flush()
# tag::cffi_funccall[]
dll.hello()
# end::cffi_funccall[]
print(
    # tag::cffi_int[]
    dll.version
    # end::cffi_int[]
)
print("end::cffi_run[]")

# tag::load_dll[]
import ctypes

dll = ctypes.CDLL(dll_path)
# end::load_dll[]

print("tag::ctypes_funccall[]")
sys.stdout.flush()
# tag::ctypes_funccall[]
dll.hello()
# end::ctypes_funccall[]
print("end::ctypes_funccall[]")

tprint(
    "ctypes_dll_resolve",
    # tag::ctypes_dll_resolve[]
    dll.version
    # end::ctypes_dll_resolve[]
)

tprint(
    "ctypes_int_resolve",
    # tag::ctypes_int_resolve[]
    ctypes.c_int.in_dll(dll, 'version')
    # end::ctypes_int_resolve[]
)

tprint(
    "ctypes_cast_resolve",
    # tag::ctypes_cast_resolve[]
    ctypes.cast(dll.version, ctypes.POINTER(ctypes.c_int))[0]
    # end::ctypes_cast_resolve[]
)
