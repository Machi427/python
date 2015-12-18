def a():
    """
    >>> a()
    Traceback (most recent call last):
       ...
    Exception: exception in c
    """
    b()

def b():
    c()

def c():
    raise Exception("exception in c")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
