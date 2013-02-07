import math

def calc(r, n):
    '''
    >>> calc(10, 6)
    60.0
    '''
    print '%.1f' % round(2*r*n*math.sin(3.14/n), 1)


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
