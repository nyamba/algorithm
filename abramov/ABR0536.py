def is_duplicated(a):
    """
    >>> is_duplicated([1, 2, 3, 4])
    NO
    >>> is_duplicated([1, 2, 3, 2])
    YES
    """

    for i in xrange(len(a)-1):
        for j in xrange(i+1, len(a)):
            if a[i] == a[j]:
                print "YES"
                return

    print "NO"


if __name__ == '__main__':
    from sys import stdin
    a = []
    l = stdin.readline()
    while l:
        a.append(int(l))
        l = stdin.readline()

    is_duplicated(a)
