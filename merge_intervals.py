def doublets(doublet):
    """
    >>> doublets([[1, 2], [3, 4]])
    [[1, 2], [3, 4]]
    >>> doublets([[1, 2], [2, 4]])
    [[1, 4]]
    >>> doublets([[1, 10], [2, 4]])
    [[1, 10]]
    >>> doublets([[0, 4], [0, 4]])
    [[0, 4]]
    """
    a = doublet[0]
    b = doublet[1]
    if a[1] < b[0]:
        return doublet
    elif b[1] > a[1] >= b[0]:
        return [[a[0], b[1]]]
    else:
        return [a]


def merge(intervals):
    """
    >>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge([[1, 4], [4, 5]])
    [[1, 5]]
    >>> merge([])
    []
    >>> merge([[1, 4], [0, 4]])
    [[0, 4]]
    >>> merge([[4, 5], [6, 7], [1, 4]])
    [[1, 5], [6, 7]]
    >>> merge([[4, 5], [1, 10], [2, 4]])
    [[1, 10]]
    >>> merge([[1, 4],[5, 6]])
    [[1, 4], [5, 6]]
    >>> merge([[1, 4], [2, 3]])
    [[1, 4]]
    """
    if not intervals:
        return intervals

    if len(intervals) == 1:
        return intervals

    intervals.sort()
    new = []
    comp = intervals[0]

    for el in intervals[1:]:
        doublet = doublets([comp, el])
        if len(doublet) == 2:
            new += doublet
            comp = el
        else:
            new += doublet
            comp = el
        return new


if __name__ == '__main__':
    import doctest
    doctest.testmod()
