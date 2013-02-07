def mod(a):
    return a if a>0 else a*(-1)


def multi(*args):
    total = 1
    for a in args:
        total *= a

    return total


def calc(*args):
    '''
    >>> calc(-500, 500)
    0.0
    500.0
    '''
    print '%.1f' % (sum(args)/len(args))
    els = [mod(i) for i in args]
    print '%.1f' % (multi(*els)**(1.0/len(args)))


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
