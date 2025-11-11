# tag::entry[]
class Entry():
    """A spec entry"""
    def provides(self): # type: () -> List[str]
        """Get the list of variables/types provided by this entry."""
        return tuple()
    def requires(self):
        """Get the list of variables/types needed by this entry."""
        return tuple()
    def write(self, out, mapper):
        """Write out an entry to the provided file handle."""
        raise NotImplementedError()
    def provides_defaults(self, mapper):
        # type: (Mapper) -> Dict[str, str]
        """Returns a dict of default values for the entry"""
        _ = mapper
        return {}
# end::entry[]

# tag::function_decl[]
class FunctionEntry(Entry):
    """Representation of a function's entry."""
    # end::function_decl[]

    def __init__(self, entry_dict):
        self.name = entry_dict['methodname_flat']
        self.params = entry_dict['params']
        self.returntype = entry_dict['returntype']

    # tag::function_requires[]
    def requires(self):
        if self.returntype == 'void':
            return (*(p['type'] for p in self.params),)
        else:
            return (self.returntype, *(p['type'] for p in self.params),)
    # end::function_requires[]

    # tag::function_provides[]
    def provides(self):
        return (self.name,)
    # end::function_provides[]

    def write(self, out, mapper):
        if self.returntype == 'void':
            restype = 'None'
        else:
            restype = mapper.resolve(self.returntype)
        out.write(f'    global {self.name}\n')
        out.write(f'    {self.name} = dll.{self.name}\n')
        out.write(f'    {self.name}.argtypes = [')
        for (i, param) in enumerate(self.params):
            out.write(f'{mapper.resolve(param["type"])}')
            if i < len(self.params) - 1:
                out.write(', ')
        out.write(']\n')
        out.write(f'    {self.name}.restype = {restype}\n')
        out.write('\n')
