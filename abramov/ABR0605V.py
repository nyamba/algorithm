def numbering(nn):
    """
    >>> numbering([100, 100, 10, 50, 5 ,1, 1])
    [200, 10, 50, 5, 2]
    >>> numbering([1, 10])
    [1, 10]
    >>> numbering([10])
    [10]
    """
    k = -1
    mm = []
    for i in xrange(len(nn)):
        if k == nn[i]:
            mm[-1] += k
        else:
            k = nn[i]
            mm.append(k)
    return mm


def romb_numb(rom):
    """
    >>> romb_numb('CCXLVII')
    247
    >>> romb_numb('XIX')
    19
    >>> romb_numb('VII')
    7
    >>> romb_numb('IX')
    9
    >>> romb_numb('XX')
    20
    """
    numbers = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    nn = numbering([numbers[x] for x in rom])
        
    k = nn[-1]
    for i in xrange(len(nn)-1):
        if nn[i] < nn[i+1]:
            k = k - nn[i]
        else:
            k = k + nn[i]

    return k

if __name__ == "__main__":
    print romb_numb(raw_input())
