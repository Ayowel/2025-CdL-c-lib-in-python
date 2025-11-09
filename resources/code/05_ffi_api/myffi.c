// https://docs.python.org/3/extending/extending.html
// Required to python <3.13
#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject * python_addme(PyObject *a, PyObject *b)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}
