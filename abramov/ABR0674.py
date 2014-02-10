def print_by(a, m):
    """
    >>> print_by([2, 4, 6], [[12, 23, 34], [1, 0, 3], [4, 5, 6]])
    12 23 34
    1 0 3
    0 5 0
    """
    for i in xrange(len(m)):
        for j in xrange(len(m)):
            if (i+j)%2 == 0 and m[i][j] in a:
                print 0,
            else:
                print m[i][j],
        print

if __name__ == '__main__':
    from sys import stdin
    a = [int(i) for i in stdin.readline().split()]
    n = int(stdin.readline())
    m = []
    for _ in xrange(n):
        m.append([int(i) for i in stdin.readline().split()])

    print_by(a, m)
