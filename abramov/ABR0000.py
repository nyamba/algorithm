def calc(a, b):
    '''
    >>> calc(1, 2)
    3
    '''
    print a + b


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
