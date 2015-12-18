#include <Python.h>

static PyObject *
dumb_print(PyObject *self, PyObject *args) {
    const char *text;
    if (!PyArg_ParseTuple(args, "s", &text))
        return NULL;
    printf("%s\n", text);
    Py_RETURN_NONE;
}

static PyMethodDef dumb_print_methods[] = {
    {"print",  dumb_print, METH_VARARGS, "Print text"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef dumb_print_module = {
    PyModuleDef_HEAD_INIT,
    "dumb_print",
    "sample extension module",
    -1,
    dumb_print_methods
};

PyMODINIT_FUNC
PyInit_dumb_print(void) {
    return PyModule_Create(&dumb_print_module);
}

