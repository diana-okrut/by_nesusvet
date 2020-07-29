def main(numbers):
    """
    >>> main([1, 1, 2, 3, 3, 4, 4, 8, 8])
    2
    >>> main([3, 3, 7, 7, 10, 11, 11])
    10
    >>> main([])
    >>> main([1])
    1
    """

    if not numbers:
        return None
    if len(numbers) == 1:
        return numbers[0]
    low, high = 1, len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = numbers[mid]
        if guess == numbers[mid - 1]:
            high = guess
        elif guess == numbers[mid + 1]:
            low = guess
        else:
            return guess


if __name__ == '__main__':
    import doctest
    doctest.testmod()
