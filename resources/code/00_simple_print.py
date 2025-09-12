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
