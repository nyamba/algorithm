import math

def calc(k, l, m, n):
    '''
    >>> calc(1, 1, 8, 8)
    YES
    >>> calc(1, 0, 8, 0)
    YES
    >>> calc(0, 0, 2, 1)
    NO
    '''
    if k == m or l == n or math.fabs(k-l) == math.fabs(m-n):
        print 'YES'
    else:
        print 'NO'



if __name__ == '__main__':
    ll = []
    import sys
    ll = [float(i) for i in sys.stdin.read().split()]
    calc(*ll[1:])


