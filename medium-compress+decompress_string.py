"""
$ python -m doctest medium-compress+decompress_string.py -v
"""

def compress_string(text):
    """
    Write a function which will "compress" input string.
    Instead of repeating a char there should be just number of repetitions.

    >>> compress_string('aaabbbbcddd')
    'a3b4cd3'
    >>> compress_string('abcdefgh')
    'abcdefgh'
    >>> compress_string('aaaaabaaaaa')
    'a5ba5'
    >>> compress_string('aaaaaaaaaab')
    'a10b'
    >>> compress_string('')
    ''
    """
    if not text:
        return text

    prev, counter = text[0], 1
    answer = []
    for char in text[1:]:
        if prev == char:
            counter += 1
            continue

        answer.append(prev + ('' if counter == 1 else str(counter)))
        prev, counter = char, 1

    answer.append(prev + ('' if counter == 1 else str(counter)))
    return ''.join(answer)


def decompress_string(text):
    """
    Write a inverse function.

    >>> decompress_string('')
    ''
    >>> decompress_string('a10b')
    'aaaaaaaaaab'
    >>> decompress_string('a5ba5')
    'aaaaabaaaaa'
    >>> decompress_string('a3b4cd3')
    'aaabbbbcddd'
    """

    if not text:
        return text

    prev, counter = text[0], ''
    answer = ''

    for char in text[1:]:
        if char.isdigit():
            counter += char
            continue
        answer += prev * (int(counter) if len(counter) >= 1 else 1)
        prev, counter = char, ''
    answer += prev * (int(counter) if len(counter) >= 1 else 1)
    return answer


if __name__ == '__main__':
    import doctest
    doctest.testmod()
