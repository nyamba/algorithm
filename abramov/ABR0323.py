def gdc(m, n):
    """
    >>> gdc(16, 8)
    8
    >>> gdc(30, 25)
    5
    >>> gdc(11, 7)
    1
    >>> gdc(2, 1)
    1
    """
    while n > 0:
        r = m % n
        m = n
        n = r

    return m


def prime_factor(n):
    """
    >>> prime_factor(45)
    [3, 5]
    >>> prime_factor(100)
    [2, 5]
    >>> prime_factor(17)
    [17]
    >>> prime_factor(12000000)
    [2, 3, 5]
    >>> prime_factor(200000000)
    [2, 5]
    """
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            if not d in factors:
                factors.append(d)
            n = n / d
        d += 1

    return factors


def calc(n):
    '''
    >>> n =100; all([gdc(n, i) == 1 for i in calc(n)])
    True
    >>> n = 1001; all([gdc(n, i) == 1 for i in calc(n)])
    True
    >>> n = 2; all([gdc(n, i) == 1 for i in calc(n)])
    True
    >>> n = 27; all([gdc(n, i) == 1 for i in calc(n)])
    True
    >>> n = 230203; all([gdc(n, i) == 1 for i in calc(n)])
    True
    >>> n = 2000000; all([gdc(n, i) == 1 for i in calc(n)])
    True
    '''
    if n < 2: yield n
    if n == 2: yield 1

    sieve = [True] * n
    factors = prime_factor(n)
    for a in factors:
        k = 1
        while a*k < n:
            sieve[a*k] = False
            k = k + 1
    for i in xrange(2, len(sieve)):
        if sieve[i]: yield i


if __name__ == "__main__":
    calc(input())
