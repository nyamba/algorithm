def calc(h):
    '''
    >>> calc(2006.09)
    20.2
    '''
    print '%.1f' % ((2*h/9.8)**0.5)


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
