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
    for i in nums:


if __name__ == '__main__':
    import doctest

    doctest.testmod()
