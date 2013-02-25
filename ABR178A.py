def calc(*a):
    '''
    >>> calc(1, 2, 3, 4)
    2
    >>> calc(1, 1, 3, 4)
    3
    '''

    count = 0
    for i in a:
        if i % 2 != 0:
            count += 1

    print count


if __name__ == '__main__':
    ll = []
    import sys
    ll = [float(i) for i in sys.stdin.read().split()]
    calc(*ll[1:])

