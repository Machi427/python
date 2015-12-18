from distutils.core import setup, Extension
setup(name='dumb_print',
      version='1.0',
      ext_modules=[Extension('dumb_print', ['dumb_print.c'])],
)