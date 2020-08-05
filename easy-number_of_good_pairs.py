def num_identical_pairs(nums):
    """
https://leetcode.com/problems/number-of-good-pairs/

    >>> num_identical_pairs([1, 2, 3, 1, 1, 3])
    4
    >>> num_identical_pairs([1, 1, 1, 1])
    6
    >>> num_identical_pairs([1, 2, 3])
    0
    >>> num_identical_pairs([1])
    0
    """

    if len(nums) == 1:
        return 0

    indecies_by_number = {}
    for i, n in enumerate(nums):
        indecies_by_number.setdefault(n, [])
        indecies_by_number[n].append(i)

    result = 0
    for indecies in indecies_by_number.values():
        if len(indecies) == 1:
            continue
        value = (len(indecies) * (len(indecies) - 1)) / 2
        result += int(value)

    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
