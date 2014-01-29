def calc(a):
    '''
    >>> calc('xerex')
    2
    >>> calc('xeroxx')
    3
    '''

    count = 0
    for i in a:
        if i == 'x':
            count += 1

    print count


if __name__ == '__main__':
    calc(raw_input())


