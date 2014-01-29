def calc(n):
    '''
    >>> calc(1924)
    4
    '''
    print n%10


if __name__ == '__main__':
    calc(*[int(i) for i in raw_input().split()])
