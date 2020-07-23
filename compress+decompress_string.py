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

    letter = text[0]
    counter = 0
    answer = ''
    buffer = []

    for i in text:
        if letter == i:
            counter += 1
            buffer = [letter, f'{counter}']
        else:
            if buffer[1] == '1':
                answer += ''.join(buffer[0])
            else:
                answer += ''.join(buffer)
            counter = 1
            buffer = [i, f'{counter}']
            letter = i
    if buffer[1] == '1':
        answer += ''.join(buffer[0])
    else:
        answer += ''.join(buffer)
    return answer


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

    answer = ''
    letter = text[0]
    quantity = ''
    buffer = [letter, quantity]

    for i in text:
        if i == letter:
            buffer[0] = i
        elif i.isdigit():
            quantity += i
            buffer[1] = quantity
        else:
            if len(buffer[1]) >= 1:
                answer += buffer[0] * int(buffer[1])
            else:
                answer += buffer[0]
            letter = i
            quantity = ''
            buffer = [letter, quantity]
    if len(buffer[1]) >= 1:
        answer += buffer[0] * int(buffer[1])
    else:
        answer += buffer[0]
    return answer


if __name__ == '__main__':
    import doctest
    doctest.testmod()
