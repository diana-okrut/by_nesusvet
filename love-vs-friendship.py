import string


def words_to_marks(word):
    alphabet = {char: i for i, char in enumerate(string.ascii_lowercase, start=1)}
    sum = 0
    for letter in word:
        if letter in alphabet:
            sum += alphabet[letter]
    return sum
