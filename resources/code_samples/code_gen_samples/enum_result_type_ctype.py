class EOS_EResult(c_int32):
    def __init__(self, value):
        if isinstance(value, c_int32):
            value = value.value
        c_int32.__init__(self, value)
    def __rrshift__(self, other):
        return other >> self.value
    def __rshift__(self, other):
        return self.value >> other
    def __rlshift__(self, other):
        return other << self.value
    def __lshift__(self, other):
        return self.value << other
    def __invert__(self):
        return EOS_EResult(~self.value)
    def __or__(self, other):
        return EOS_EResult(self.value | other)
    def __ror__(self, other):
        return EOS_EResult(other | self.value)
    def __int__(self):
        return self.value
