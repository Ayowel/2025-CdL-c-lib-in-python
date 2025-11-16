# Code from scripts/build.py

# tag::indexation[]
# Load all header files
files_index = build_header_file_index(dir_path)
# Pick a read order for the header files
files_order = build_file_read_order(files_index)
# end::indexation[]

# tag::eos_base_override[]
# Override eos_base as it mostly provides hard-to-parse definitions.
assert 'eos_base.h' in files_order
files_index['eos_base.h'] = [
    'typedef int32_t EOS_Bool;',
    '#define EOS_TRUE ((EOS_Bool)1)',
    '#define EOS_FALSE ((EOS_Bool)0)',
]
# end::eos_base_override[]

# tag::eos_result_parse[]
def parse_result_value(content, i, line, comment = '', file = ''):
    """Extract an EOS_RESULT enum value from a list of lines"""
    _ = (content, file)
    valinfo = re.match('^EOS_RESULT_VALUE(_LAST)?\\((?P<name>[a-zA-Z0-9_]+), (?P<value>[x0-9A-F]+)\\)$', line)
    assert valinfo
    name = valinfo['name'].strip()
    value = valinfo['value'].strip()
    return (i, OrderedDict(
        comment = comment,
        name = name,
        value = value
    ))
# end::eos_result_parse[]

# tag::line_start_flags[]
flags = [
    ('EOS_DECLARE_FUNC', parse_function, partial(assert_insert, functions, 'methodname_flat')),
    ('EOS_DECLARE_CALLBACK', parse_callback, partial(assert_insert, callbacks, 'callbackname')),
    ('EOS_STRUCT', parse_struct, partial(assert_insert, structs, 'struct')),
    ('EOS_RESULT_VALUE', parse_result_value, partial(assert_insert, SCOPED_ENUMS['EOS_EResult'], 'name')),
    ('PROCESS_CATEGORY', parse_log_enum_value, partial(assert_insert, SCOPED_ENUMS['EOS_ELogCategory'], 'name')),
    ('EOS_ENUM_START', parse_enum_start_end, partial(assert_insert, enums, 'enumname')),
    ('EOS_ENUM_END', parse_enum_start_end, noop),
    ('EOS_ENUM_BOOLEAN_OPERATORS', parse_skip_line, noop),
    ('EOS_ENUM', parse_enum, partial(assert_insert, enums, 'enumname')),
    ('#define', parse_define, partial(assert_insert_if, defines, DEFINES_IGNORE_LIST, 'name')),
    (('typedef', 'EOS_EXTERN_C'), parse_typedef, partial(assert_insert, typedefs, 'name')),
    (DIRECTIVES_IGNORE_LIST, absorb_directive, noop)
]
# end::line_start_flags[]
