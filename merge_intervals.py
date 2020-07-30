def merge(intervals):
    """
    >>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge([[1, 4], [4, 5]])
    [[1, 5]]
    >>> merge([])
    []
    """
    if not intervals:
        return intervals
    new = []
    comp = intervals[0]
    for el in intervals[1:]:
        if comp[1] >= el[0]:
            comp[1] = el[1]
            del el
            new.append(comp)
        else:
            new.append(el)
            comp = el
    return new


if __name__ == '__main__':
    import doctest
    doctest.testmod()
