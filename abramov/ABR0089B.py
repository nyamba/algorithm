def gcd(n, m):
    '''
    Greates common divisor
    '''

    maxi = max(n, m)
    mini = min(n, m)

    while mini:
        swap = maxi % mini
        maxi = mini
        mini = swap

    return maxi


def calc(a, b):
    '''
    Least Common Multiple

    >>> calc(26, 32)
    416
    >>> calc(2, 5)
    10
    >>> calc(1, 5)
    5
    >>> calc(0, 5)
    0
    >>> calc(5, 5)
    5
    '''
    print (a * b)/gcd(a, b)


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])

