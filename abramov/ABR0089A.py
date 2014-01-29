def calc(n, m):
    '''
    >>> calc(56, 108)
    4
    >>> calc(15, 6)
    3
    >>> calc(6, 6)
    6
    >>> calc(2, 5)
    1
    >>> calc(0, 5)
    5
    '''

    maxi = max(n, m)
    mini = min(n, m)

    while mini:
        swap = maxi % mini
        maxi = mini
        mini = swap

    print maxi


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
