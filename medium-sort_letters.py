def sort_letters(text):
    """
    >>> sort_letters('aaabccccdeefffff')
    'fffffccccaaaeebd'
    >>> sort_letters('abcdefghijklmnop')
    'abcdefghijklmnop'
    >>> sort_letters('')
    ''
    >>> sort_letters('aba')
    'aab'
    >>> sort_letters('abcabccba')
    'aaabbbccc'
    """
    if not text:
        return text

    letters_dict = {}
    for i in text:
        letters_dict.setdefault(i, 1)
        letters_dict[i] += 1
    letters = list(zip(letters_dict.values(), letters_dict.keys()))
    return letters
