import math

def calc(a, h, n):
    '''
    >>> calc(0, 0.1, 10)
    9.8
    '''
    n = int(n)
    f = lambda x: (x**2 + 1)*math.cos(x)**2

    total = 0
    for i in range(n+1):
        total += f(a+i*h)

    print round(total, 1)


if __name__ == '__main__':
    import sys
    calc(*[float(i) for i in sys.stdin.read().split()])
