def calc(n):
    '''
    >>> calc(10)
    1
    >>> calc(93)
    9
    >>> calc(2010)
    2
    >>> calc(4000020)
    4
    '''

    while n > 9:
        n = int(n / 10)

    print n



if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])


