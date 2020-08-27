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
        if symbol in {'(', ')'}
    ]

    if not bracket_in_text:
        return True

    stack = []
    for el in bracket_in_text:
        if el == '(':
            stack.append(el)
        else:
            if not stack:
                return False
            stack.pop(-1)

    return not stack


if __name__ == '__main__':
    import doctest

    failures, errors = doctest.testmod()
