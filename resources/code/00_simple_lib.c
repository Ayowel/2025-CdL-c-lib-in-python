#include <stdio.h>
#include <stdlib.h>
#include "00_simple_lib.h"

// tag::function[]
void hello() {
    printf("Hello world!\n");
    fflush(stdout);
}
// end::function[]

// tag::const[]
const int version = 2;
// end::const[]

// Returns a list item with value between 0 and 2*PI.
// This function is only here to ensure that the absence of defines, structs,
// and typedefs in the lib's symbols is not due to them being unused.
struct linked_list* normalized_radians_list_item(float degree) {
    float radians = degree * PI / 180;
    radians = radians - 2*PI*(int)(radians / 2 / PI);
    struct linked_list* v = calloc(sizeof(struct linked_list), 1);
    v->value = ternary(radians > 0, radians, radians + 2 * PI);
    v->next = NULL;
    return v;
}
