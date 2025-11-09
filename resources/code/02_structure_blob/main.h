#include <stdint.h>
// tag::pragma[]
#pragma pack(1)
// end::pragma[]

// tag::datablob_struct[]
typedef struct {
  char a;
  uint32_t b;
  char c;
  char d;
} DataBlob;
// end::datablob_struct[]

// tag::datablob_function_declaration[]
char DataBlob_get_d(DataBlob* blob);
// end::datablob_function_declaration[]
