#include <stdint.h>
// tag::api_tick[]
void api_tick();
// end::api_tick[]

// tag::api_callback[]
typedef void api_callback(uint32_t evt, void* data); 
// end::api_callback[]
// tag::api_setup_callback[]
void api_setup_callback(api_callback callback, void* data);
// end::api_setup_callback[]
