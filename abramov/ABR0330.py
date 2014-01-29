def calc(n):
    '''
    >>> calc(7)
    6
    >>> calc(100)
    6
    28
    >>> calc(28)
    6
    '''
    p_numbers = [
            6,
            28,
            496,
            8128,
            33550336,
            8589869056,
            ]
    for i in p_numbers:
        if i < n:
            print i


if __name__ == '__main__':
    import sys
    ll = [int(i) for i in sys.stdin.read().split()]
    calc(*ll)
