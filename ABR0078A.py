def calc(a, n):
    '''
    >>> calc(9.81, 4)
    9261.4
    >>> calc(1.0, 5)
    1.0
    '''
    total = 1.0
    while n > 0:
        total *= a
        n -= 1

    print round(total, 1)


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])

