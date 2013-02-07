def mod(a):
    return a if a>0 else a*(-1)

def calc(a ,b):
    '''
    >>> calc(-3.1, 12.24)
    -0.2
    '''
    print '%.1f' % ((mod(a)-mod(b))/(1+mod(a*b)))


if __name__ == '__main__':
    a, b = [float(i) for i in raw_input().split()]
    calc(a, b)
