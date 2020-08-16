def main(monsters):
    """
    https://codeforces.com/contest/1334/problem/C

    >>> main([(7, 15), (2, 14), (5, 3)])
    6
    >>> main([(9, 44), (18, 3), (5, 2), (1, 3), (5, 7), (9, 11)])
    7
    """

    start_index = monsters.index(min(monsters))
    new_monsters_list = monsters[start_index::] + monsters[:start_index]

    result = 0
    damage = 0
    for monster, dam in new_monsters_list:
        monster -= damage
        if monster > 0:
            result += monster
        damage = dam

    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
