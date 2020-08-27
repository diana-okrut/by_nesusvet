from collections import Counter


def is_balanced(text):
    """
    See https://www.codewars.com/kata/all-that-is-open-must-be-closed-dot-dot-dot

    >>> is_balanced('')
    True
    >>> is_balanced('Sensei says yes!')
    True
    >>> is_balanced('))((')
    False
    >>> is_balanced('(Sensei says yes!)')
    True
    >>> is_balanced('(Sensei says no!')
    False
    >>> is_balanced('(Sensei) (says) (yes!)')
    True
    >>> is_balanced('(Sensei (says) yes!)')
    True
    >>> is_balanced('((Sensei) says) no!)')
    False
    >>> is_balanced('(Sensei (says) (yes!))')
    True
    """

    bracket_in_text = [
        symbol
        for symbol in text
        if symbol in ['(', ')']
    ]

    if not bracket_in_text:
        return True

    if bracket_in_text[0] == ')':
        return False

    if len(bracket_in_text) % 2 != 0:
        return False

    counter = Counter(bracket_in_text)
    if counter['('] != counter[')']:
        return False

    stack = []
    for el in bracket_in_text:
        if el == '(':
            stack.append(el)
        else:
            stack.pop(-1)

    return not stack


if __name__ == '__main__':
    import doctest

    failures, errors = doctest.testmod()
