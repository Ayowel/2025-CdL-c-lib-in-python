#!/usr/bin/env python
import cffi
import ctypes
import os

dll_path = f"{os.path.splitext(__file__)[0]}.so"

def test_cffi_datablob(PACK=1):
    # tag::cffi_build[]
    ffi = cffi.FFI()
    ffi.cdef(f'''
        typedef struct {{
        char a;
        uint32_t b;
        char c;
        char d;
        }} DataBlob;
        char DataBlob_get_d(DataBlob* blob);
        ''', pack = PACK)
    dll = ffi.dlopen(dll_path)
    # end::cffi_build[]

    # tag::cffi_datablob_instance[]
    d = ffi.new('DataBlob *')
    d.a = b'a'
    d.b = int.from_bytes(b'fghi')
    d.c = b'c'
    d.d = b'd'
    # end::cffi_datablob_instance[]

    return (
        # tag::cffi_run[]
        dll.DataBlob_get_d(d)
        # end::cffi_run[]
    )

def test_ctypes_datablob(PACK=1):
    dll = ctypes.CDLL(dll_path)
    # tag::ctypes_datablob_class[]
    class DataBlob(ctypes.Structure):
        _pack_ = PACK
        _fields_ = [
            ('a', ctypes.c_char),
            ('b', ctypes.c_uint32),
            ('c', ctypes.c_char),
            ('d', ctypes.c_char),
        ]
    # end::ctypes_datablob_class[]

    # tag::ctypes_function[]
    dll.DataBlob_get_d.argtypes = [ctypes.POINTER(DataBlob)]
    dll.DataBlob_get_d.restype = ctypes.c_char
    # end::ctypes_function[]

    # tag::ctypes_datablob_instance[]
    d = DataBlob(b'a', int.from_bytes(b'fghi'), b'c', b'd')
    # end::ctypes_datablob_instance[]
    return (
        # tag::ctypes_datablob_call[]
        dll.DataBlob_get_d(ctypes.byref(d))
        # end::ctypes_datablob_call[]
    )

print("tag::ctypes_datablob[]")
for i in (1, 2, 4, 8):
    print(f'PACK {i} - {test_ctypes_datablob(i)}')
print("end::ctypes_datablob[]")

print("tag::cffi_datablob[]")
for i in (1, 2, 4, 8):
    print(f'PACK {i} - {test_cffi_datablob(i)}')
print("end::cffi_datablob[]")
