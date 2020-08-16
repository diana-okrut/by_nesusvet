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

    g = sorted(g)
    s = sorted(s)
    result = 0
    g_index = 0
    s_index = 0
    while g_index < len(g) and s_index < len(s):
        cookie = s[s_index]
        greed = g[g_index]
        if cookie < greed:
            s_index += 1
        else:
            result += 1
            s_index += 1
            g_index += 1

    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
