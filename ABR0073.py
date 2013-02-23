def calc(k, l):
    '''
    >>> calc(28, 31)
    31 31
    >>> calc(9, 9)
    0 0
    '''

    if k != l:
        print max(k, l), max(k, l)
    else:
        print 0, 0


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
