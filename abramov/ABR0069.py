def calc(ot):
    '''
    >>> calc(1.72)
    1.8
    3 17
    >>> calc(6.28)
    0.0
    12 0
    >>> calc(0)
    0.0
    0 0
    '''

    pi = 3.14

    all_minut = (720/(2*pi))*ot
    hour = int(all_minut/60.0)
    minut = int((all_minut/60.0 - hour)*60)
    minut_ot = ((2*pi)/60) * minut

    print '%.1f' % minut_ot
    print hour, minut


if __name__ == '__main__':
    calc(*[float(i) for i in raw_input().split()])
