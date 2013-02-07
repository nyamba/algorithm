import string
from collections import Counter

small_letters = string.letters[:26]

def calc_beaty(val):
    only_letters = filter(lambda a: a in small_letters, val.lower())
    c = Counter(only_letters)
    max_beaty = 26
    total_beaty = 0

    for (char, count) in c.most_common():
        total_beaty += count * max_beaty
        max_beaty -= 1

    return total_beaty


def main():
    case_count = int(raw_input())
    vals = []
    for _ in xrange(case_count):
        vals.append(raw_input())

    for i in xrange(len(vals)):
        print 'Case #%d: %d' % (i+1, calc_beaty(vals[i]))


if __name__ == '__main__':
    main()
