def calc(a, b, r, s):
    '''
    >>> calc(12, 6, 0, 1)
    R
    >>> calc(13, 6, 0, 1)
    S
    >>> calc(14, 6, 0, 1)
    No solution
    '''
    if a % b == r:
        print 'R'
    elif a % b == s:
        print 'S'
    else:
        print 'No solution'



if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
