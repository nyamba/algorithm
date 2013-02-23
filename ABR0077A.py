def calc(n):
    '''
    >>> calc(8)
    256
    >>> calc(1)
    2
    >>> calc(0)
    1
    '''

    result = 1

    while n:
        n -= 1
        result *= 2

    print result


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
