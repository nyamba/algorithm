def calc(st):
    '''
    >>> calc('1,2,-3,-4,-5')
    YES
    >>> calc(',-')
    YES
    >>> calc('new,  -earht-')
    NO
    '''

    leng = len(st)
    for i in xrange(leng-1):
        if st[i] == ',' and st[i+1] == '-':
            print 'YES'
            return

    return 'NO'


if __name__ == '__main__':
    import sys
    calc(sys.stdin.read())

