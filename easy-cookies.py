"""
See the original https://leetcode.com/problems/assign-cookies/
"""


def find_content_children(g, s):
    """
    >>> find_content_children([1,2,3], [1,1])
    1
    >>> find_content_children([1,2], [1,2,3])
    2
    >>> find_content_children(list(range(1, 11)), [1] * 100 + list(range(1, 11)))
    10
    >>> find_content_children([2, 3, 4, 2], [1, 1, 1, 1])
    0
    >>> find_content_children([1, 2, 3, 4, 5], [5, 5, 3, 3, 1])
    5
    >>> find_content_children([1, 2, 3, 4, 5], [])
    0
    """
    if not s or not g:
        return 0

    if len(s) == 1:
        for item in g:
            return 1 if s[0] >= item else 0

    g = sorted(g)
    s = sorted(s)
    result = 0
    if len(g) == len(s):
        for item_g, item_s in zip(g, s):
            if item_g <= item_s:
                result += 1
        return result

    # if len(g) > len(s):
    #     return result
    #
    # if len(s) > len(g):
    #     return result
