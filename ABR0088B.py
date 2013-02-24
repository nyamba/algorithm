def calc(n):
    '''
    >>> calc(140)
    41
    >>> calc(14000)
    41
    >>> calc(104)
    401
    >>> calc(1)
    1
    >>> calc(0)
    0
    >>> calc(5431)
    1345
    '''
    result = 0
    while n > 0:
        result = result * 10 + (n % 10)
        n = n / 10

    print result


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
