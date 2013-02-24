def calc(a):
    '''
    >>> calc([1.0, 1.0, 2.0])
    2.0
    '''
    total = 1
    for i in a:
        total *= i

    print '%.1f' % total


if __name__ == '__main__':
    raw_input()
    calc([float(i) for i in raw_input().split()])
