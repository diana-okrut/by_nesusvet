def main(text: str) -> bool:
    """
    Implement a function which will check if it is possible to build a valid
    palindrome from a sequence of letters. Only permutations are allowed.
    >>> main("anna")
    True
    >>> main("nana")
    True
    >>> main("nanam")
    True
    >>> main("dogo")
    False
    """

    counting_by_letters = {}

    for i in text:
        counting_by_letters.setdefault(i, 0)
        counting_by_letters[i] += 1
    counter = 0
    for j in counting_by_letters.values():
        if j % 2 != 0:
            counter += 1
        if counter > 1:
            return False
    result = []
    len_new_result = 0
    for key, value in counting_by_letters.items():
        len_new_result += value
        if value % 2 == 0:
            new_key = key * (value // 2)
            result.append(new_key)
            result.insert(0, new_key)
        elif (value % 2 != 0) and (value // 2 == 0):
            center = len(result) // 2
            result = result[0:center] + [key] + result[center::]
        elif (value % 2 != 0) and (value // 2 != 0):
            new_key = key * (value // 2)
            result.append(new_key)
            result.insert(0, new_key)
            center = len(result) // 2
            result = result[0:center] + [key] + result[center::]
    text_result = "".join(result)
    return text_result
