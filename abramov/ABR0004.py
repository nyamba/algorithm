def multi(*args):
    total = 1
    for a in args:
        total *= a

    return total


def calc(*args):
    '''
    >>> calc(1206.0, 2006)
    1606.0
    1555.4
    '''
    print '%.1f' % (sum(args)/len(args))
    print '%.1f' % (multi(*args)**(1.0/len(args)))


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
