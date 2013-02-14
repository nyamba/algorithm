def calc(x, y):
    '''
    >>> calc(75, 79)
    75.0
    79.0
    >>> calc(79, 75)
    79.0
    '''
    if x > y:
        print '%.1f' % x
    else:
        print '%.1f\n%.1f' % (x, y)


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
