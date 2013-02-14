def calc(*ags):
    '''
    >>> calc(1, 2, 3)
    NO
    >>> calc(3, 4, 5)
    YES
    '''

    args = list(ags)
    l = len(list(args))
    for _ in xrange(l):
        if args[0] >= sum(args[1:]):
            print 'NO'
            return
        args[0], args[l-1] = args[l-1], args[0]

    print 'YES'


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
