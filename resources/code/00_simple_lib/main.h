// tag::defines[]
#define PI 3.14159265359
#define ternary(cond, if_true, if_false) (cond?if_true:if_false)
// end::defines[]

// tag::typedef[]
typedef void* MyHandle;
// end::typedef[]

// tag::struct[]
struct linked_list {
    int value;
    struct linked_list* next;
};
// end::struct[]

// tag::function[]
void hello();
// end::function[]

// tag::const[]
const int version;
// end::const[]
