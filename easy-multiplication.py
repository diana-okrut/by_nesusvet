def main(numbers):
    """
    Given a sequence of integers. Build a new sequence of the same length. Each element of a new
    sequence should be calculated as a multiplication of elements of the original sequence except
    the element with the same index.  Think about possible corner cases.

    >>> main([1, 2, 0, 0])
    [0, 0, 0, 0]
    >>> main([1, 0, 2])
    [0, 2, 0]
    >>> main([1, 2, 3])
    [6, 3, 2]
    >>> main([])
    []
    """
    zero_count = numbers.count(0)  # O(n)
    if zero_count > 1:
        return [0] * len(numbers)

    total = 1
    for i in numbers:  # O(n)
        if i != 0:
            total *= i  # O(1)

    if zero_count == 1:
        mem = numbers.index(0)  # O(n)
        answer = [0] * len(numbers)
        answer[mem] = total
        return answer

    return [total // n for n in numbers]  # O(n)

    # answer = []
    # for i in numbers:
    #     answer.append(int(total / i))
    # return answer
