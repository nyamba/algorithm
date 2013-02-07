def calc(a, b):
    '''
    >>> calc(1.6, 2.74)
    3.2
    2.2
    '''
    print '%.1f' % ((a**2 + b**2)**0.5)
    print '%.1f' % ((a*b)/2.0)


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
