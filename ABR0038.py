def calc(x, y):
    '''
    >>> calc(45, 61)
    17.0
    '''
    if x > y:
        print '%.1f' % (x-y)
    else:
        print '%.1f' % ((y-x)+1)


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
