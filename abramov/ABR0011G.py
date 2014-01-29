import math


def calc(x, y, z):
    '''
    >>> calc(0.0, 2.0, 0.0)
    2.0
    1.0
    '''
    print '%.1f' % (y + x/(y**2 + math.fabs(x**2/(y+x**3/3))))
    print '%.1f' % (1 + math.tan(z/2)**2)


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
