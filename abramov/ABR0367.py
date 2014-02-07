def numb_table(a):
    """
    >>> numb_table([3, 2, 1])
    -6 -3 0
    -7 -4 -1
    -8 -5 -2
    """
    for i in xrange(3):
        for j in xrange(3):
            print a[i] - 3*a[j],
        print


if __name__ == "__main__":
    from sys import stdin
    numb_table([int(i) for i in stdin.read().split()])
