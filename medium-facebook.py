def main(text: str) -> bool:
    """
    Implement a function which will check if it is possible to build a valid
    palindrome from a sequence of letters. Only permutations are allowed.
    >>> main("anna")
    True
    >>> main("nana")
    True
    >>> main("nanam")
    True
    >>> main("dogo")
    False
    """

    counting_by_letters = {}
    for i in text:
        counting_by_letters.setdefault(i, 0)
        counting_by_letters[i] += 1
    counter = 0
    for j in counting_by_letters.values():
        if j % 2 != 0:
            counter += 1
    return False if counter > 1 else True
