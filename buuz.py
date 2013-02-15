def calc(*args):
    '''
    >>> calc(3, 5, 15, 7)
    buuz
    piiz
    buuzpiiz
    7
    '''
    for c in args:
        msg = ''
        if c % 3 == 0:
            msg = 'buuz'
        if c % 5 == 0:
            msg += 'piiz'

        if not msg:
            print c
        else:
            print msg


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
