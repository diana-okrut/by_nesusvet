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
        if el[1] >= comp[1] >= el[0]:
            comp[1] = el[1]
            new.append(comp)
        elif el[1] <= comp[1] >= el[0]:
            continue
        else:
            new.append(el)
            comp = el
    return new


if __name__ == '__main__':
    import doctest
    doctest.testmod()
