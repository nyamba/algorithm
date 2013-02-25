def calc(*a):
    '''
    >>> calc(8.0, -9, 3.3, 1, 10.234)
    -9.0
    '''

    mini = a[0]
    for i in a:
        if i < mini:
            mini = i

    print round(mini, 1)


if __name__ == '__main__':
    import sys
    ll = [float(i) for i in sys.stdin.read().split()]
    calc(*ll[1:])

