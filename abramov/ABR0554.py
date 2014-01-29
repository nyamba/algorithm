def sqr_list(n):
    '''
    >>> sqr_list(25)
    [4, 9, 16, 25]
    >>> sqr_list(20)
    [4, 9, 16]
    '''
    ll = []
    for i in xrange(2, int(n**0.5)+1):
        a = i**2
        if a <= n:
            ll.append(a)

    return ll


def is_sqr(n):
    '''
    >>> is_sqr(4)
    True
    >>> is_sqr(5)
    False
    '''

    return int(n**0.5)**2 == n


def calc(n):
    '''
    >>> calc(15)
    3 4 5
    5 12 13
    6 8 10
    9 12 15
    '''
    for a in xrange(3, n+1):
        pass


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
