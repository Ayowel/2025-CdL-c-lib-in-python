#!/usr/bin/env python
import ctypes
import gc
import os

dll_path = f"{os.path.splitext(__file__)[0]}.so"
dll = ctypes.CDLL(dll_path)

api_callback = ctypes.CFUNCTYPE(None, ctypes.c_uint32, ctypes.c_void_p)
dll.api_setup_callback.argtypes = [api_callback, ctypes.c_void_p]
dll.api_setup_callback.restype = None
dll.api_tick.argtypes = []
dll.api_tick.restype = None

# tag::datablob_class[]
class DataBlob(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_char),
        ('b', ctypes.c_uint32),
        ('c', ctypes.c_char),
        ('d', ctypes.c_char),
    ]
# end::datablob_class[]

library = dict()

# tag::api_callback_function[]
@api_callback
def api_python_callback(event, data):
    data = ctypes.cast(data, ctypes.POINTER(DataBlob))
    if data:
        print(f'Received event {event} with data {data.contents.c}.')
    else:
        print(f'Received event {event} with NO data.')
# end::api_callback_function[]

# tag::api_tick_only[]
dll.api_tick()
# end::api_tick_only[]

print("tag::api_tick_cb[]")
# tag::api_tick_cb[]
dll.api_setup_callback(api_python_callback, None)
dll.api_tick()
# end::api_tick_cb[]
print("end::api_tick_cb[]")

print("tag::api_tick_data[]")
# tag::api_tick_data[]
data = DataBlob(b'a', int.from_bytes(b'fghi'), b'c', b'd')
dll.api_setup_callback(api_python_callback, ctypes.cast(ctypes.byref(data), ctypes.c_void_p))
dll.api_tick()
# end::api_tick_data[]
print("end::api_tick_data[]")

print("tag::call_callback_function[]")
# tag::call_callback_function[]
def call_callback():
    d = DataBlob(b'a', int.from_bytes(b'fghi'), b'c', b'd')
    dll.api_setup_callback(api_python_callback, ctypes.cast(ctypes.byref(d), ctypes.c_void_p))
# end::call_callback_function[]
print("end::call_callback_function[]")

print("tag::call_callback[]")
# tag::call_callback[]
call_callback()
dll.api_tick()
# end::call_callback[]
print("end::call_callback[]")
