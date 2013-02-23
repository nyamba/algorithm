def calc(x):
    '''
    >>> calc(4)
    EVEN
    >>> calc(5)
    ODD
    '''

    if x % 2 == 0:
        print 'EVEN'
    else:
        print 'ODD'


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
