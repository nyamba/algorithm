def calc(n):
    """
    >>> calc(18)
    2
    3
    >>> calc(64)
    2
    """
    k = 2
    while n > 1:
        if n % k == 0:
            print k
            while n % k == 0:
                n = n / k
        k += 1

if __name__ == '__main__':
    calc(input())
