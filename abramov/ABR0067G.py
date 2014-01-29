def calc(n):
    '''
    >>> calc(31)
    3
    >>> calc(9)
    9
    >>> calc(100)
    1
    '''

    if n < 10:
        print n
    elif n < 100:
        print int(n/10)
    else:
        print int(n/100)



if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
