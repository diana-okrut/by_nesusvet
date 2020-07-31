def main(numbers):
    """
    >>> main([])
    >>> main([1])
    1
    >>> main([1, 1, 2])
    2
    >>> main([1, 2, 2, 3 ,3])
    1
    >>> main([1, 1, 2, 2, 3])
    3
    >>> main([3, 3, 7, 7, 10, 11, 11])
    10
    >>> main([3, 3, 7, 10, 10, 11, 11])
    7
    >>> main([1, 1, 2, 3, 3, 4, 4, 8, 8])
    2
    >>> main([1, 1, 2, 2, 3, 3, 5, 5, 6, 9, 9])
    6
    >>> main([1, 1, 2, 2, 3, 5, 5, 6, 6, 9, 9])
    3
    """
    if not numbers:
        return None

    if len(numbers) == 1:
        return numbers[0]

    left, right = 0, len(numbers) - 1
    while (right - left) > 2:  # O(log(n))
        mid = (left + right) // 2  # O(1)
        guess = numbers[mid]  # O(1)

        if guess == numbers[mid - 1]:  # O(1)
            if mid % 2 == 0:  # O(1)
                right = mid
            else:
                left = mid + 1
        elif guess == numbers[mid + 1]:  # O(1)
            if mid % 2 == 0:
                left = mid
            else:
                right = mid - 1
        else:
            return guess
    l, m, r = numbers[left], numbers[left+1], numbers[right]  # O(1)
    if l == m:
        return r
    else:
        return l


if __name__ == '__main__':
    import doctest
    doctest.testmod()
