def selection(vals):
    '''

    vals[0] = min(vals[0:])
    vals[1] = min(vals[1:])
    vals[2] = min(vals[2:])
            ...
    vals[n] = min(vals[n:])

    worst case performance:     o(n^2)
    best case performance:      o(n^2)
    average case performance:   o(n^2)

    >>> selection([3, 4, 5, 3])
    [3, 3, 4, 5]
    >>> selection([3, 2, 1, 1])
    [1, 1, 2, 3]
    >>> selection([0])
    [0]
    >>> selection([])
    []
    >>> selection([1, 2, 3, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> selection([1, 1, 1, 1, 1, 1])
    [1, 1, 1, 1, 1, 1]
    '''

    leng = len(vals)
    offset = 0

    for i in xrange(leng):
        min_i = offset
        for j in xrange(offset+1, leng):
            if vals[min_i] > vals[j]:
                min_i = j

        vals[offset], vals[min_i] = vals[min_i], vals[offset]
        offset += 1

    return vals


def insertion(vals):
    '''
    >>> insertion([3, 4, 5, 3])
    [3, 3, 4, 5]
    >>> insertion([3, 2, 1, 1])
    [1, 1, 2, 3]
    >>> insertion([0])
    [0]
    >>> insertion([])
    []
    >>> inseriton([1, 2, 3, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> insertion([1, 1, 1, 1, 1, 1])
    [1, 1, 1, 1, 1, 1]
    '''

    leng = len(vals)
    offset = 1

    for i in xrange(1, leng):
        for j in xrange(i):
            if vals[j] > vals[i]:


if __name__ == '__main__':
    import doctest
    doctest.testmod()
