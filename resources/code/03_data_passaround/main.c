#include <stddef.h>
#include "main.h"

// tag::vars[]
api_callback* api_registered_cb = NULL;
void* api_registered_data = NULL;
// end::vars[]

// tag::api_tick[]
void api_tick() {
    if (api_registered_cb != NULL) {
        api_registered_cb(0, api_registered_data);
        api_registered_cb = NULL;
        api_registered_data = NULL;
    }
}
// end::api_tick[]

// tag::api_setup_callback[]
void api_setup_callback(api_callback* callback, void* data) {
    api_registered_data = data;
    api_registered_cb = callback;
}
// end::api_setup_callback[]
