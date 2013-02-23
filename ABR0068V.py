def calc(n):
    '''
    >>> calc(289)
    YES
    >>> calc(28)
    NO
    >>> calc(1234)
    YES
    '''

    ll = []

    for _ in xrange(4):
        p = n % 10
        if p in ll:
            print 'NO'
            return
        ll.append(p)
        n = int(n / 10)

    print 'YES'


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
