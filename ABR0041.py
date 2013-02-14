def calc(*args):
    '''
    >>> calc(3.14, 1, 1.5)
    1.5
    '''
    for i in args:
        if i > 1 and i < 3:
            print '%.1f' % i


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
