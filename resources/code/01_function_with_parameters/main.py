#!/usr/bin/env python
import cffi
import ctypes
import os

dll_path = f"{os.path.splitext(__file__)[0]}.so"

def tprint(tag, text):
    print(f"tag::{tag}[]\n{text}\nend::{tag}[]")

# tag::cffi_build[]
ffi = cffi.FFI()
ffi.cdef('''
    int double_int(int);
    float double_float(float);
    ''')
dll = ffi.dlopen(dll_path)
# end::cffi_build[]

tprint(
    "cffi_double_int",
    # tag::cffi_double_int[]
    dll.double_int(3)
    # end::cffi_double_int[]
)
tprint(
    "cffi_double_float",
    # tag::cffi_double_float[]
    dll.double_float(3.5)
    # end::cffi_double_float[]
)


dll = ctypes.CDLL(dll_path)

tprint(
    "ctypes_double_int",
    # tag::ctypes_double_int[]
    dll.double_int(3)
    # end::ctypes_double_int[]
)

try:
    # tag::ctypes_double_float[]
    dll.double_float(3.5)
    # end::ctypes_double_float[]
    raise Exception("Failed to fail")
except ctypes.ArgumentError as e:
    tprint(
        "ctypes_double_float",
        "{}.{}: {}".format(e.__class__.__module__, e.__class__.__name__, e)
    )

tprint(
    "ctypes_double_float_ctypes",
    # tag::ctypes_double_float_ctypes[]
    dll.double_float(ctypes.c_float(3.5))
    # end::ctypes_double_float_ctypes[]
)

# tag::ctypes_double_float_return_type[]
dll.double_float.restype = ctypes.c_float
# end::ctypes_double_float_return_type[]
tprint(
    "ctypes_double_float_return_typed",
    # tag::ctypes_double_float_return_typed[]
    dll.double_float(ctypes.c_float(3.5))
    # end::ctypes_double_float_return_typed[]
)

# tag::ctypes_double_float_arg_type[]
dll.double_float.argtypes = [ctypes.c_float]
# end::ctypes_double_float_arg_type[]
tprint(
    "ctypes_double_float_arg_typed",
    # tag::ctypes_double_float_arg_typed[]
    dll.double_float(3.5)
    # end::ctypes_double_float_arg_typed[]
)
