def kids_with_candies(candies, extra_candies):
    """
    https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
    >>> kids_with_candies([2, 3, 5, 1, 3], 3)
    [True, True, True, False, True]
    >>> kids_with_candies([4, 2, 1, 1, 2], 1)
    [True, False, False, False, False]
    >>> kids_with_candies([12, 1, 12], 10)
    [True, False, True]
    """
    maximum = max(candies)
    answer = []
    for kid in candies:
        if kid + extra_candies >= maximum:
            answer.append(True)
        else:
            answer.append(False)
    return answer


if __name__ == '__main__':
    import doctest

    doctest.testmod()
