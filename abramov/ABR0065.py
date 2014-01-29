def calc(n):
    '''
    >>> calc(12)
    NO
    >>> calc(1)
    YES
    '''
    sum = 0
    for i in str(n):
        sum = sum + int(i)**3

    if n**2 == sum:
        print 'YES'
    else:
        print 'NO'


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
