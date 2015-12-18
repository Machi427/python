#include <Python.h>

typedef struct {
    PyObject_HEAD
} spam_object;

static PyTypeObject spam_type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "spam.Spam",               /* tp_name */
    sizeof(spam_object),       /* tp_basicsize */
    0,                         /* tp_itemsize */
    0,                         /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,        /* tp_flags */
    "Spam objects",            /* tp_doc */
};

static PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",
    "Example module that creates an extension type.",
    -1,
    NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    PyObject* m;

    spam_type.tp_new = PyType_GenericNew;
    if (PyType_Ready(&spam_type) < 0)
        return NULL;

    m = PyModule_Create(&spammodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&spam_type);
    PyModule_AddObject(m, "Spam", (PyObject *)&spam_type);
    return m;
}

