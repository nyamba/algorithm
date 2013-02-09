def calc(x, y, z):
    '''
    >>> calc(1, 1, 1)
    3.0
    '''
    print '%.1f' % max(x+y+z, x*y*z)


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
