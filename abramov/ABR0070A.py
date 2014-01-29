def calc(h, m):
    """
    >>> calc(3, 0)
    17
    >>> calc(3, 30)
    52
    >>> calc(4, 0)
    22
    >>> calc(12, 0)
    0
    >>> calc(11, 59)
    1
    >>> calc(11, 54)
    6
    >>> calc(12, 59)
    7
    """
    mdegree = 360.0*m/60
    if h == 12:
        h = 0
    hdegree = 360.0*h/12 + mdegree*30/360.0
    vh = 0.5
    vm = 6

    ddegree = hdegree - mdegree
    if ddegree < 0:
        ddegree += 360.0

    x = (ddegree * vh)/(vm - vh)
    minute = (x + ddegree) / 6.0
    if int(minute) < minute:
        minute += 1

    return int(minute)

    
if __name__ == '__main__':
    import sys
    h, m = (int(a) for a in sys.stdin.read().split())
    print calc(h, m)
