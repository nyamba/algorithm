def calc(*args):
    '''
    >>> calc(19.05, 800, 500)
    NO
    >>> calc(19.05, 200, 500)
    YES
    >>> calc(19.05, 19.05, 500)
    NO
    '''

    print 'YES' if args[0] < args[1] and args[1] < args[2] else 'NO'


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
