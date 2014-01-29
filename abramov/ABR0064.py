def calc(n):
    '''
    >>> calc(1924)
    19
    '''
    print int(n/100)


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
