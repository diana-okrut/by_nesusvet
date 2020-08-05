def running_sum(nums):
    """
    https://leetcode.com/problems/running-sum-of-1d-array/

     >>> running_sum([1, 2, 3, 4])
     [1, 3, 6, 10]
     >>> running_sum([1, 1, 1, 1, 1])
     [1, 2, 3, 4, 5]
     >>> running_sum([3, 1, 2, 10, 1])
     [3, 4, 6, 16, 17]
     """
    _sum = 0
    result = []
    for n in nums:
        result.append(n + _sum)
        _sum += n
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
