def reverse_bit(m):
    """
    >>> reverse_bit(6)
    3
    >>> reverse_bit(8)
    1
    >>> reverse_bit(9)
    9
    >>> reverse_bit(7)
    7
    >>> reverse_bit(0)
    0
    """
    a = []
    while m > 0:
        if a or m%2 == 1:
            a.append(m%2)
        m = m / 2

    n  = 0
    for i in xrange(len(a)-1, -1, -1):
        n = n + a[i]*(2**(len(a)-1-i))

    return n

if __name__ == "__main__":
    print reverse_bit(input())
