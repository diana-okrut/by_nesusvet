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
    count = 0
    new = []
    for i in nums:
        new.append(i + count)
        count += i
    return new


if __name__ == '__main__':
    import doctest

    doctest.testmod()
