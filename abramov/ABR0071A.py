def calc(a):
    """
    >>> calc(3.1) == calc(0.1)
    True
    >>> calc(1.6) != calc(-1.6)
    True
    >>> calc(3.1)
    -0.2
    >>> calc(3.1232323)
    -0.3
    >>> calc(1.5)
    0.0
    >>> calc(1.5) == calc(-4.5)
    True
    >>> calc(1.6)
    -0.2
    >>> calc(1.5)
    0.0
    >>> calc(0.0)
    0.0
    """
    p = int(a/1.5)
    x = a - (1.5 * p)
    value = x**3 - 2.25*x 
    return round(value, 1)


if __name__ == '__main__':
    import sys
    print calc(float(sys.stdin.read()))
