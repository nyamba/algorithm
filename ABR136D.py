def calc(*a):
    '''
    >>> calc(3.14, 9.81, 0.5)
    106.3
    '''

    sumi = 0
    for i in a:
        sumi += i*i

    print round(sumi, 1)


if __name__ == '__main__':
    ll = []
    import sys
    ll = [float(i) for i in sys.stdin.read().split()]
    calc(*ll[1:])

