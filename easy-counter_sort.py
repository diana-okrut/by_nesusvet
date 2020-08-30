def counter_sort(numbers):
    """
    >>> counter_sort([2, 1, 4, 3, 6, 5])
    [1, 2, 3, 4, 5, 6]
    >>> counter_sort([10, 15, 13, 12, 11, 14])
    [10, 11, 12, 13, 14, 15]
    >>> counter_sort([0, -10, 1, 2, 3, -5])
    [-10, -5, 0, 1, 2, 3]
    >>> counter_sort([])
    []
    """

    if not numbers:
        return numbers

    counter = dict.fromkeys(range(min(numbers), max(numbers) + 1), 0)

    for el in numbers:
        counter[el] += 1

    result = []

    for key, value in counter.items():
        if value > 0:
            result += [key] * value
    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
