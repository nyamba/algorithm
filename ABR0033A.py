def calc(a, b):
    '''
    >>> calc(3.14, 1.4)
    3.1
    '''
    print '%.1f' % max([a, b])


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
