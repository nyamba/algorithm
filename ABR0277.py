def calc(*a):
    '''
    >>> calc(1, 2, 3, 4, 5)
    5.0 4.0 3.0 2.0 1.0
    '''

    leng = len(a)
    for i in xrange(leng):
        print round(a[leng-i-1], 1),


if __name__ == '__main__':
    import sys
    ll = [float(i) for i in sys.stdin.read().split()]
    calc(*ll)


