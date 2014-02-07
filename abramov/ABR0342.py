def average_x(a, m):
    '''
    >>> average_x(3.0, [4.0323, 3.4, 22.3, 1.0])
    4.0
    1.0
    '''

    minum = a - (m[0] + m[1])/2
    index = [0, 1]
    if minum < 0: minum *= -1

    for i in xrange(len(m)-1):
        for j in xrange(i+1, len(m)): 
            k = a - (m[i] + m[j])/2
            if k < 0 :
                k = -1 * k
            if minum > k:
                index = [i, j]
                minum = k

    print round(m[index[0]], 1)
    print round(m[index[1]], 1)


if __name__ == "__main__":
    from sys import stdin
    a = float(stdin.readline())
    m = []
    for i in xrange(25):
        m.append(float(stdin.readline()))

    average_x(a, m)
