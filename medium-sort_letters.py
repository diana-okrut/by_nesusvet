def sort_letters(text):
    """
    Return a string of the same letters where all the letters are sorted by
    its frequency in descending order. In case of equal frequency letters
    should go in the order they were met in the original string.

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

    freq_by_letter = {}
    for i in text:
        freq_by_letter.setdefault(i, 0)
        freq_by_letter[i] += 1

    index_by_letter = {}
    for index, char in enumerate(text):
        index_by_letter.setdefault(char, index)

    unsorted = []
    for letter, freq in freq_by_letter.items():
        value = (freq, -index_by_letter[letter], letter)
        unsorted.append(value)

    pairs = sorted(unsorted, reverse=True)
    # sorted() делает копию, не модиф нативный объект
    # letters.sort(reverse=True) # модифицирует объект, невозможно использовать нативный
    result = []
    for freq, _, letter in pairs:
        result.append(letter * freq)
    return ''.join(result)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
