def shuffle(nums, n):
    """
    https://leetcode.com/problems/shuffle-the-array/

    >>> shuffle([2, 5, 1, 3, 4, 7], 3)
    [2, 3, 5, 4, 1, 7]
    >>> shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)
    [1, 4, 2, 3, 3, 2, 4, 1]
    >>> shuffle([1, 1, 2, 2], 2)
    [1, 2, 1, 2]
    """
    answer = []
    for value in nums[:n]:
        answer.append(value)
        answer.append(nums[n])
        n += 1
    return answer


if __name__ == '__main__':
    import doctest

    doctest.testmod()
