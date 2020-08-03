def main(A: str, B: str) -> bool:
    """
    >>> main("abcdea", "acbeda")
    False
    >>> main("ab", "ab")
    False
    >>> main("aa", "aa")
    True
    >>> main("aaaaaaabc", "aaaaaaacb")
    True
    >>> main("", "aa")
    False
    >>> main("abcdea", "acbdea")
    True
    >>> main("abab", "abab")
    True
    >>> main("acccccb", "bccccca")
    True
    >>> main("abcaa", "abcbb")
    False
    """
    if len(A) != len(B):
        return False
    if set(A) != set(B):
        return False
    if A == B:
        return True if len(A) != len(set(A)) else False

    index = 0
    different_letter_A = ''
    different_letter_B = ''
    for letter in A:
        if letter == B[index]:
            index += 1
        else:
            different_letter_A += letter
            different_letter_B += B[index]
            index += 1

    return True if len(different_letter_A) == 2 and different_letter_A == different_letter_B[::-1] else False




if __name__ == '__main__':
    import doctest
    doctest.testmod()
