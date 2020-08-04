def merge_two(a, b):
    """
    https://leetcode.com/problems/merge-intervals/
    >>> merge_two([1, 2], [3, 4])
    [[1, 2], [3, 4]]
    >>> merge_two([1, 2], [2, 4])
    [[1, 4]]
    >>> merge_two([1, 3], [2, 4])
    [[1, 4]]
    >>> merge_two([1, 10], [2, 4])
    [[1, 10]]
    >>> merge_two([0, 4], [0, 4])
    [[0, 4]]
    """
    a_start, a_end = a
    b_start, b_end = b
    if a_end < b_start:
        return [a, b]
    elif a_end >= b_start:
        return [[a_start, max(a_end, b_end)]]


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

    intervals = sorted(intervals)

    current = intervals[0]

    result = []
    for interval in intervals[1:]:
        merge_result = merge_two(current, interval)
        if len(merge_result) > 1:
            result.append(current)
            current = interval
        else:
            current = merge_result[0]
    result.append(current)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
