# tag::function_mapping[]
# Associate each function to its corresponding class
for funcname, function in functions_index.items():
    base_split_name = funcname.split('_')
    for i in range(2, len(base_split_name))[::-1]:
        found = False
        # Match from the function's name or from its "handle" version
        for split_name in (base_split_name[:i], (base_split_name[0], f'H{base_split_name[1]}', *base_split_name[2:i])):
            contextname = '_'.join(split_name)
            if contextname in enum_types_structs_index:
                obj = enum_types_structs_index[contextname]
                local_name = '_'.join(base_split_name[i:])
                is_static = contextname in function.returntype
                obj.add_function(function, local_name, is_static)
                found = True
                break
        if found:
            break
    else:
        logger.info('No context object found for function %s.', funcname)
# end::function_mapping[]

# tag::render[]
out.write(FILE_START)
out.write('\n')
# Add 'blank' function entries
for e in self.file_entries:
    if isinstance(e, FunctionEntry):
        out.write(f'{e.name} = not_ready\n')
# Write out every entry
for e in self.file_entries:
    if not isinstance(e, FunctionEntry):
        e.write(out, self.mapper)
# Load fuction pointers from dll
out.write('def load(dll):\n')
for e in self.file_entries:
    if isinstance(e, FunctionEntry):
        e.write(out, self.mapper)
# end::render[]
