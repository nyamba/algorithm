def is_triple(n):
    """
    >>> is_triple(5)
    'YES'
    >>> is_triple(3)
    'YES'
    >>> is_triple(7)
    'NO'
    """
    x = 1
    nn = 1

    for i in xrange(1, n+1):
        nn *= i

    k = 6
    while k <= nn:
        if k == nn:
            return "YES"
        x += 1
        k = x*(x+1)*(x+2)

    return "NO"


if __name__ == "__main__":
    print is_triple(input())
