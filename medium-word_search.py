def main(board, word):
    """
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCED")
    True
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "SEE")
    True
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCBQ")
    False
    >>> main([['A','A','A'],['A','A','A'],['A','A','A']], "A" * 100)
    False
    """

    count_by_letter = {}
    for i in word:
        count_by_letter.setdefault(i, 0)
    for element in board:
        for letter in element:
            if letter in count_by_letter:
                count_by_letter[letter] += 1

    if 0 in count_by_letter.values():
        return False

    # find all first letters in the matrix [(x, y), (x1, y1)]
    found = find_all_item_positions(board, word[0])
    for x, y in found:
        path = []
        if search(board, word, 1, x, y, path):
            return True
    return False


def search(matrix, word, index, x, y, path):
    path.append((x,y))
    if index == len(word) - 1:
        return True

    letter = word[index]
    # посмотреть какие буквы кругом
    connected = find_connected_positions(matrix, x, y)

    # сравнить все найденные буквы со next буквой из слова
    candidates = []
    for i, j in connected:
        if letter == matrix[i][j]:
            candidates.append((i, j))

    # если да, то перейти на координату этой буквы and continue
    for i, j in candidates:
        if (i,j) in path:
            continue
        result = search(matrix, word, index + 1, i, j, path)
        if result:
            return True
    else:
        return False


def find_connected_positions(matrix, x, y):
    """
    >>> find_connected_positions([[0]], 0, 0)
    []
    >>> find_connected_positions([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 0, 0)
    [(1, 0), (0, 1)]
    >>> find_connected_positions([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 2, 2)
    [(1, 2), (2, 1)]
    >>> find_connected_positions([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1)
    [(0, 1), (2, 1), (1, 0), (1, 2)]
    """
    result = []
    # сверху
    if x > 0:
         result.append((x - 1, y))
    # снизу
    if x < len(matrix) - 1:
        result.append((x + 1, y))
    # слева
    if y > 0:
        result.append((x, y - 1))
    # справа
    if y < len(matrix[0]) - 1:
        result.append((x, y + 1))
    return result


def find_all_item_positions(matrix, item):
    """
    >>> find_all_item_positions([[0]], 0)
    [(0, 0)]
    >>> find_all_item_positions([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 2)
    [(0, 2)]
    >>> find_all_item_positions([[3, 1, 2], [3, 4, 5], [6, 3, 8]], 3)
    [(0, 0), (1, 0), (2, 1)]
    """
    result = []
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if item == element:
                result.append((i, j))
    return result
