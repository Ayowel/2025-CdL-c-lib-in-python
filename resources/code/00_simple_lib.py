#!/usr/bin/env python
import os

dll_path = f"{os.path.splitext(__file__)[0]}.so"

# tag::load_dll[]
import ctypes

dll = ctypes.CDLL(dll_path)
# end::load_dll[]

# tag::funccall[]
dll.hello()
# end::funccall[]

print(
    # tag::dll_resolve[]
    dll.version
    # end::dll_resolve[]
)

print(
    # tag::int_resolve[]
    ctypes.c_int.in_dll(dll, 'version')
    # end::int_resolve[]
)

print(
    # tag::cast_resolve[]
    ctypes.cast(dll.version, ctypes.POINTER(ctypes.c_int))[0]
    # end::cast_resolve[]
)
