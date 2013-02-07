import string
from collections import Counter

allowed_chars = string.letters +' :'
pps = ['(', ')']


def remove_char(string, index):
    '''
    >>> remove_char('abcc', 0)
    'bcc'
    >>> remove_char('abcc', 1)
    'acc'
    >>> remove_char('abcc', 3)
    'abc'
    '''
    return string[:index] + string[index+1:]


def has_valid_chars(vals):
    for c in vals:
        if c not in allowed_chars:
            return False

    return True


def remove_nice_p(vals, has_open=False):
    '''
    >>> remove_nice_p('hello')
    'hello'
    >>> remove_nice_p('hello (')
    'hello ('
    >>> remove_nice_p('hello :)')
    'hello :)'
    >>> remove_nice_p('(hello)')
    'hello'
    >>> remove_nice_p('(hello :) )')
    'hello : )'
    >>> remove_nice_p('hello (good)')
    'hello good'
    >>> remove_nice_p('hello (:')
    'hello (:'
    >>> remove_nice_p('hello (: (good)')
    'hello : (good'
    >>> remove_nice_p('hello (good (cool) yep :) yah)')
    'hello good cool yep : yah)'
    >>> remove_nice_p(')(')
    ')('
    >>> remove_nice_p('(1)2)3(4)')
    '12)34'
    '''
    c = Counter(vals)
    remove_count = min(c[')'], c['('])
    for _ in xrange(remove_count):
        open_i = vals.index('(')
        try:
            close_i = open_i + vals[open_i:].index(')')
            vals = remove_char(vals, open_i)
            vals = remove_char(vals, close_i-1)
        except:
            break

    return vals


def read_cases():
    case_count = int(raw_input())
    cases = []
    for _ in xrange(case_count):
        cases.append(raw_input())

    return cases


def is_balanced(val):
    new = remove_nice_p(val)
    new = new.replace(':)', '').\
            replace(':(', '')
    try:
        assert ')' not in new
        assert '(' not in new
        assert has_valid_chars(new)
    except:
        return 'NO'

    return 'YES'


def main():
    cases = read_cases()
    for i in xrange(len(cases)):
        print 'Case #%d: %s' % (i+1, is_balanced(cases[i]))


if __name__ == '__main__':
    #import doctest; doctest.testmod()
    main()
