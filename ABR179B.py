def calc(*a):
    '''
    >>> calc(8, 9, 8, 2, 8, 4)
    5
    '''

    count = 0
    for i in a:
        if i % 7 in [1, 2, 5]:
            count += 1

    print count


if __name__ == '__main__':
    import sys
    ll = [float(i) for i in sys.stdin.read().split()]
    calc(*ll[1:])
