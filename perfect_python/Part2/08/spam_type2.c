#include <Python.h>

typedef struct {
    PyObject_HEAD
} spam_object;

static PyObject *
ham_method(PyObject* self) {
    return PyUnicode_FromString("hello");
}

static PyMethodDef spam_methods[] = {
    {"ham", (PyCFunction)ham_method, METH_NOARGS, "Doc string of ham"},
    {NULL}  /* Sentinel */
};

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
    Py_TPFLAGS_DEFAULT |
        Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "spam objects",            /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    spam_methods,              /* tp_methods */
    0,                         /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    0,                         /* tp_init */
    0,                         /* tp_alloc */
    0,                         /* tp_new */
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

