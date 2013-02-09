def calc(*args):
    '''
    >>> calc(12.06, 80, 19.21)
    80.0
    '''
    print '%.1f' % max(args)


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
