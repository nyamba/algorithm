def calc_z(b, r, n):
    '''
    >>> calc_z(2, 3, 0)
    1
    >>> calc_z(2, 3, 1)
    5
    >>> calc_z(2, 3, 2)
    19
    >>> calc_z(2, 3, 3)
    65
    '''
    if n == 0:
        return 1
    elif n == 1:
        return b + r

    z = (b**n) + (r**n)

    for i in xrange(1, n):
        z += (b**i) * (r**(n-i))

    return z


def calc_element(a, b, r, c, i):
    '''
    >>> calc_element(34, 37, 656, 97, 0)
    34
    >>> calc_element(34, 37, 656, 97, 1)
    71
    '''
    if i == 0:
        return a

    return ((b**i)*a + c*calc_z(b, r, i-1))%(r**i)


def calculate(val):
    '''
    >>> calculate([97, 39, 34, 37, 656, 97])
    8
    '''
    n, k, a, b, c, r = val
    ll = range(n)
    prev = a
    l = []
    for i in xrange(k):
        l.append(prev)
        prev = (b*prev +c)%r

    print l
    return min(ll)


def read_cases():
    case_count = int(raw_input())
    cases = []
    for _ in xrange(case_count):
        c = []
        c += [int(i) for i in raw_input().split()]
        c += [int(i) for i in raw_input().split()]
        cases.append(c)

    return cases


def main():
    cases = read_cases()
    for i in xrange(len(cases)):
        print 'Case #%d: %d' % (i+1, calculate(cases[i]))


if __name__ == '__main__':
    import doctest; doctest.testmod()
    #main()
