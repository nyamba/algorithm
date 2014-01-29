def calc(n):
    '''
    >>> calc(31)
    2
    >>> calc(9)
    1
    '''
    print len(str(n))


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
