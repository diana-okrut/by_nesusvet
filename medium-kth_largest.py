def kth_largest(numbers, k):
    """
    See https://leetcode.com/problems/kth-largest-element-in-an-array/
    >>> kth_largest([3, 2, 1, 5, 6, 4], 2)
    5
    >>> kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4
    >>> kth_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    9
    >>> kth_largest([10, 9, 5, 6, 4, 7, 2, 1, 3, 8], 3)
    8
    >>> kth_largest([], 0)
    0
    >>> kth_largest([0, -10, 1, 2, 3, -5], 6)
    -10
    """
    if not numbers:
        return 0

    counter = dict.fromkeys(range(max(numbers), min(numbers) - 1, -1), 0)

    for el in numbers:
        counter[el] += 1

    result = []

    for key, value in counter.items():
        if value > 0:
            result += [key] * value
        if len(result) >= k:
            return result[k - 1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
