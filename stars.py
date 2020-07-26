def stars(text):
    """
    >>> stars('2 3')
    <
    >>> stars('1 1')
    =
    >>> stars('100 1')
    >
    """
    char = text.split()
    a = int(char[0]) ** int(char[1])
    b = int(char[1]) ** int(char[0])
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')
    return


if __name__ == '__main__':
    import doctest
    doctest.testmod()
