def is_rectangle(a):
    """
    >>> is_rectangle([1, 2, 3, 4])
    YES
    >>> is_rectangle([5, 6, 7, 89])
    NO
    """
    if max(a) < sum(a) - max(a):
        print "YES"
    else:
        print "NO"

if __name__ == "__main__":
    from sys import stdin
    is_rectangle([int(i) for i in stdin.read().split()])
