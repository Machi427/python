def safe_str(s):
    """
    >>> print(safe_str(None))
    <BLANKLINE>
    >>> print(safe_str("test"))
    test
    """
    if s is None:
        return ""
    else:
        return s

if __name__ == '__main__':
    import doctest
    doctest.testmod()
