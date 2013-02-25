def calc(n):
    '''
    >>> calc(1960)
    961
    >>> calc(8)
    8
    '''
    str_n = str(n)
    new_str = str_n[-1]+str_n[1:-1]
    if len(str_n) > 1:
        new_str += str_n[0]

    print int(new_str)


if __name__ == '__main__':
    import sys
    calc(int(sys.stdin.read()))
