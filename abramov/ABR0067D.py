def calc(n):
    '''
    >>> calc(100)
    0
    >>> calc(98)
    9
    '''

    if n < 100:
        print n/10
    else:
        print n/10%10


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])

