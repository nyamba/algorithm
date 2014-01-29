def calc(*a):
    '''
    >>> calc(8.0, 9, 3.3, 1, 10.234)
    10.2
    '''

    maxi = None
    for i in a:
        if i > maxi:
            maxi = i

    print round(maxi, 1)


if __name__ == '__main__':
    import sys
    ll = [float(i) for i in sys.stdin.read().split()]
    calc(*ll[1:])
