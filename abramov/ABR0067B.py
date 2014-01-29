def calc(n):
    '''
    >>> calc(9)
    9
    >>> calc(28)
    10
    >>> calc(100)
    1
    '''

    total = 0

    while n:
        p = n % 10
        n = int(n / 10)
        total += p

    print total


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
