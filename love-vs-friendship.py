import string


def words_to_marks(word):
    alphabet = {
        char: i
        for i, char in enumerate(string.ascii_lowercase, start=1)
    }
    sum = 0
    for letter in word:
        if letter in alphabet:
            sum += alphabet[letter]
    return sum
    # values = []
    # for letter in word:
    #     if letter in alphabet:
    #         values.append(alphabet[letter])
    values = [alphabet[letter] for letter in word if letter in alphabet]
    return sum(values)
