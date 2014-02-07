def numb_table(n):
    """
    >>> numb_table(3)
    0.50 0.33 0.25
    0.33 0.25 0.20
    0.25 0.20 0.17
    """
    for i in xrange(1, n+1):
        for j in xrange(1, n+1):
            print '%.2f' % round(1.0/(i+j), 2),
        print


if __name__ == '__main__':
    numb_table(input())
