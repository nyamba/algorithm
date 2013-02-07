def calculate():
    pass


def read_cases():
    case_count = int(raw_input())
    cases = []
    for _ in xrange(case_count):
        cases.append(raw_input())

    return cases


def main():
    cases = read_cases()
    for i in xrange(len(cases)):
        print 'Case #%d: %s' % (i+1, calculate(cases[i]))


if __name__ == '__main__':
    #import doctest; doctest.testmod()
    main()
