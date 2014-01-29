def calc(n):
    '''
    >>> calc(1990)
    4
    '''

    count = 0

    while n:
        n = int(n / 10)
        count += 1

    print count


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
