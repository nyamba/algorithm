def calc(*a):
    '''
    >>> calc(3.0, 0.0, 3.4, 5.51)
    5.5
    >>> calc(3.2)
    3.2
    >>> calc()
    '''

    maxi = None

    for i in a:
        if i > maxi:
            maxi = i

    if maxi:
        print round(maxi, 1)


if __name__ == '__main__':
    import sys
    ll = [float(i) for i in sys.stdin.read().split()]
    if ll[0]:
        calc(*ll[1:])
