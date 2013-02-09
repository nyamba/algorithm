def calc(*args):
    '''
    >>> calc(800, 2006091327, 2008010128)
    419.8
    '''
    print '%.1f' % (6.67*(10**-11)*args[1]*args[2]/args[0]**2)


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
