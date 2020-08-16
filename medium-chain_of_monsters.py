def main(monsters):
    """
    https://codeforces.com/contest/1334/problem/C

    >>> main([(7, 15), (2, 14), (5, 3)])
    6
    >>> main([(9, 44), (18, 3), (5, 2), (1, 3), (5, 7), (9, 11)])
    7
    """

    start_index = monsters.index(min(monsters))

    for item in monsters[:start_index]:
        monsters.append(monsters.pop(monsters.index(item)))

    result = 0
    damage = 0
    for monster, dam in monsters:
        monster -= damage
        while monster > 0:
            monster -= 1
            result += 1
        else:
            damage = dam

    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
