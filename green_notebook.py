def green_notebook(parameters):
    """
    >>> green_notebook('2 3 4')
    3
    >>> green_notebook('2 3 6')
    6
    >>> green_notebook('1 4 2')
    2
    >>> green_notebook('7 2 10')
    7
    """
    n = int(parameters.split()[0])
    m = int(parameters.split()[1])
    k = int(parameters.split()[2])
    list_with_character = []
    for symbol_1 in range(1, n+1):
        list_with_character.append(symbol_1)
        for symbol_2 in range(2, m+1):
            list_with_character.append(symbol_1 * symbol_2)
    list_with_character = sorted(list_with_character)

    return list_with_character[k-1]
