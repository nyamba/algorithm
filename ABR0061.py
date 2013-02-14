import math


def calc(x):
    '''
    >>> calc(1.6)
    1
    2
    1
    >>> calc(100.5)
    100
    101
    100
    >>> calc(-1.6)
    -2
    -2
    -1
    '''

    print int(math.floor(x))
    print int(round(x))
    print int(x)


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
