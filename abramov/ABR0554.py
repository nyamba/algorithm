def multiple(m, n):
    a = n[0][0]*m[0] + n[0][1]*m[1] + n[0][2]*m[2]
    b = n[1][0]*m[0] + n[1][1]*m[1] + n[1][2]*m[2]
    c = n[2][0]*m[0] + n[2][1]*m[1] + n[2][2]*m[2]

    return a, b, c


def gen_prime(parent):
    A = ([1, -2, 2],
         [2, -1, 2],
         [2, -2, 3])
    B = ([1, 2, 2],
         [2, 1, 2],
         [2, 2, 3])
    C = ([-1, 2, 2],
         [-2, 1, 2],
         [-2, 2, 3])

    c1 = multiple(parent, A)
    c2 = multiple(parent, B)
    c3 = multiple(parent, C)

    return c1, c2, c3


if __name__ == '__main__':
    n = input()
    parents = [(3, 4, 5)]
    all_ptriples = []

    # generating primes
    index = 0
    while index < len(parents):
        for c in gen_prime(parents[index]):
            cc = sorted(c)
            if cc[2] <= n:
                parents.append(cc)
        index += 1

    # scaling the primes
    append = all_ptriples.append
    for i in parents:
        scale = 1
        while i[2]*scale <= n:
            append((scale*i[0], scale*i[1], scale*i[2]))
            scale += 1

    # sorting
    all_ptriples.sort()

    for a, b, c in all_ptriples:
        print a, b, c
