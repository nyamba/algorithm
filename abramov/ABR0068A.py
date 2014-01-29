def calc(n):
    '''
    >>> calc(31)
    NO
    >>> calc(9119)
    YES
    >>> calc(110)
    YES
    '''
    l1 = n/1000%10
    l2 = n/100% 10
    l3 = n/10%10
    l4 = n%10

    if l1 == l4 and l2 == l3:
        print 'YES'
    else:
        print 'NO'


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
