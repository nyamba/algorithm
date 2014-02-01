def calc(a):
    """
    >>> calc([1.0, 2.0, 3.0])
    1.7 1.3 1.0
    """
    total = sum(a)
    for i in range(len(a)):
        print round((total - a[i])/len(a), 1),

if __name__ == "__main__":
    import sys
    calc([float(i) for i in sys.stdin.read().split()])
