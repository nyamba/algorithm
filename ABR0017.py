def calc(r):
    '''
    >>> calc(126.202)
    48754.607
    '''
    print '%.3f' % (3.14*r**2 - 1256)


if __name__ == '__main__':
    import sys
    calc(float(sys.stdin.read()))

