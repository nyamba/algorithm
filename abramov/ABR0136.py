def calc(*a):
    '''
    >>> calc(2.15, 3.56, 6.49, 4.82)
    17.0
    '''

    sumi = 0
    for i in a:
        sumi += i

    print round(sumi, 1)


if __name__ == '__main__':
    ll = []
    import sys
    ll = [float(i) for i in sys.stdin.read().split()]
    calc(*ll[1:])
