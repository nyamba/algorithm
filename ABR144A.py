def calc(n):
    '''
    >>> calc(1)
    0
    1
    >>> calc(5)
    0
    1
    1
    2
    3
    5
    '''
    fib_list = [0, 1]
    for i in xrange(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    for i in fib_list:
        print i


if __name__ == '__main__':
    import sys
    calc(int(sys.stdin.read()))

