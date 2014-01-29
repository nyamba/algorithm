def calc(a ,b):
    '''
    >>> calc(10.4, 3.6)
    14.1
    6.9
    37.8
    '''
    print '%.1f' % (a+b)
    print '%.1f' % (a-b)
    print '%.1f' % (a*b)


if __name__ == '__main__':
    #import doctest; doctest.testmod()
    a, b = [float(i) for i in raw_input().split()]
    calc(a, b)
