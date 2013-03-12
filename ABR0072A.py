def calc(a):
    '''
    >>> calc(2)
    1.0
    >>> calc(0)
    1.0
    >>> calc(-1)
    0.0
    >>> calc(1.5)
    0.8
    >>> calc(-3)
    0.0
    >>> calc(-4)
    1.0
    '''
    x = ((a + 1)% 2 + 2)%2 -1

    print round(-(x**2) + 1, 1)


if __name__ == '__main__':
    import sys
    calc(*[float(i) for i in sys.stdin.read().split()])
