def calc(k, l, m, n):
    '''
    >>> calc(7, 5, 8, 7)
    NO
    >>> calc(7, 5, 7, 5)
    YES
    '''
    if (k+l)%2 == (m+n)%2:
        print 'YES'
    else:
        print 'NO'


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])

