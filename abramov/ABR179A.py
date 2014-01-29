def calc(*a):
    '''
    >>> calc(1, 9, 4, 1, 6, 2, 2)
    3
    >>> calc(5, 14)
    1
    '''
    count = 0

    for i in a:
        if i % 2 == 0 and ((i/2) % 2 == 1):
            count += 1

    print count


if __name__ == '__main__':
    import sys
    calc(*[int(i) for i in sys.stdin.read().split()][1:])


