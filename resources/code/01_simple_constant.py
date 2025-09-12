#!/usr/bin/env python
import ctypes
import os

dll_path = f"{os.path.splitext(__file__)[0]}.so"

dll = ctypes.CDLL(dll_path)
# tag::dll_resolve[]
print(dll.version)
# end::dll_resolve[]
# tag::int_resolve[]
print(ctypes.c_int.in_dll(dll, 'version'))
# end::int_resolve[]
# tag::cast_resolve[]
print(ctypes.cast(dll.version, ctypes.POINTER(ctypes.c_int))[0])
# end::cast_resolve[]
