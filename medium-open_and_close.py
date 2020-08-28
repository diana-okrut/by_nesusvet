def is_balanced(text, brackets):
    """
    See https://www.codewars.com/kata/all-that-is-open-must-be-closed-dot-dot-dot

    >>> is_balanced('', '()')
    True
    >>> is_balanced('Sensei says yes!', '()')
    True
    >>> is_balanced('))((', '()')
    False
    >>> is_balanced('(Sensei says yes!)', '()')
    True
    >>> is_balanced('(Sensei says no!', '()')
    False
    >>> is_balanced('(Sensei) (says) (yes!)', '()')
    True
    >>> is_balanced('(Sensei (says) yes!)', '()')
    True
    >>> is_balanced('((Sensei) says) no!)', '()')
    False
    >>> is_balanced('(Sensei (says) (yes!))', '()')
    True
    >>> is_balanced('(Sensei [says] {yes!})', '()[]{}')
    True
    >>> is_balanced('(Sensei [says) {yes!}]', '()[]{}')
    False
    >>> is_balanced('a az az z', 'az')
    True
    >>> is_balanced('Banzai!', '!!')
    False
    >>> is_balanced('!Banzai!', '!!')
    True
    >>> is_balanced('(Sensei !says! {!yes!})', '(){}!!')
    True
    """
    # разделить открывающие и закрывающие скобки
    opening, closing = brackets[::2], brackets[1::2]
    opening_by_closing = dict(zip(closing, opening))
    opening_set = set(opening)

    # отфильтровать только значимые символы
    brackets_set = set(brackets)
    bracket_in_text = [
        symbol
        for symbol in text  # O(n)
        if symbol in brackets_set  # O(1)
    ]
    if not bracket_in_text:
        return True

    stack = []
    # stack = Stack()
    for el in bracket_in_text:  # O(n)
        if el in opening_set and el in opening_by_closing:  # corner case
            if stack and opening_by_closing[el] == stack[-1]:
                stack.pop()
            else:
                stack.append(el)

        elif el in opening_set:  # новая открывающая скобка
            stack.append(el)

        else:  # закрывающая скобка
            if not stack:
                return False  # закрывающая скобка без открывающей

            # map => hashmap => dict
            # matching_open = opening[closing.index(el)]
            if opening_by_closing[el] != stack[-1]:  # закрывающая скобка совпадает с открывающей
                return False

            stack.pop()

    return not stack


if __name__ == '__main__':
    import doctest

    failures, errors = doctest.testmod()
