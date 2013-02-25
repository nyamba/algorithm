def calc(st):
    '''
    >>> calc('1+*,2,-3,-4,-5')
    2
    >>> calc(',-')
    0
    '''

    count = 0
    for i in st:
        if i in ['*', '+']:
            count += 1

    print count


if __name__ == '__main__':
    import sys
    calc(sys.stdin.read())
