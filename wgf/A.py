def green_notebook(param):
    """
    >>> green_notebook('6 12')
    4
    >>> green_notebook('6 52')
    0

    """
    n = int(param.split()[0])
    k = int(param.split()[1])

    if k == 1:
        return 1

    if n * n < k:
        return 0

    result = 0
    for i in range(n, 0, -1):
        if (k % i == 0) and (k // i <= n):
            result += 1
    return result
