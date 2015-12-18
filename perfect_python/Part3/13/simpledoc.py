def fizzbuzz(num):
    """
    >>> fizzbuzz(0)
    'FizzBuzz'
    >>> fizzbuzz(2)
    '2'
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(4)
    '4'
    >>> fizzbuzz(5)
    'Buzz'
    >>> fizzbuzz(6)
    'Fizz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

if __name__ == '__main__':
    from doctest import testmod
    testmod()
