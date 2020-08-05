def main(A: str, B: str) -> bool:
    """
    https://leetcode.com/problems/buddy-strings

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
        return len(A) != len(set(A))

    different_letter_A = []
    different_letter_B = []

    for a_char, b_char in zip(A, B):
        if a_char != b_char:
            different_letter_A.append(a_char)
            different_letter_B.append(b_char)

    return (
            len(different_letter_A) == 2
            and different_letter_A == different_letter_B[::-1]
    )


if __name__ == '__main__':
    import doctest
    doctest.testmod()
