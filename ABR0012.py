def calc(a):
    '''
    >>> calc(4)
    6.9
    '''
    print '%.1f' % (((3*(a**2)/4)**0.5) * (a/2))


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
