def calc(n, k, p, a):
    '''
    speed - 2n

    >>> calc(7, 2, 6, [1, 2, 3, 4, 5, 7, 7])
    1 3 4 5 6 7 7
    >>> calc(7, 2, 9, [1, 2, 3, 4, 5, 7, 7])
    1 3 4 5 7 7 9
    '''

    l = []
    for i in xrange(n):
        if i != k-1:
            l.append(a[i])

    swap = p
    for i in xrange(n-1):
        if l[i] > p:
            swap = l[i]
            l[i] = p
            p = swap
            print l[i],
        else:
            print l[i],

    print swap,


if __name__ == '__main__':
    n, k, p = (int(i) for i in raw_input().split())
    a = [int(i) for i in raw_input().split()]
    calc(n, k, p, a)
