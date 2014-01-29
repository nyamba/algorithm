def calc(*args):
    '''
    >>> calc([100.5, 100], [50.9, 50])
    83.2
    151.4
    '''
    vol = sum(zip(*args)[0])
    temp = (sum(map(lambda a: a[0]*a[1], args))*1.0)/vol
    print '%.1f' % temp
    print '%.1f' % vol


if __name__ == '__main__':
    input = []
    input.append([float(i) for i in raw_input().split()])
    input.append([float(i) for i in raw_input().split()])
    calc(*input)
