import itertools


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.abc = alphabet
        # make a dict of letter's numbers from alphabet
        self.number_by_letter = {}
        for i, char in enumerate(self.abc):
            self.number_by_letter[char] = i
        # make a reversed dict
        self.letter_by_number = {value: key for key, value in self.number_by_letter.items()}

    def encode(self, text):
        # convert all chars to codes
        if text.isupper():
            return text
        codes = [self.number_by_letter[char] for char in text]

        # print(codes)

        # find new codes for each letter
        key_num = [self.number_by_letter[letter] for letter in self.key]
        # print(key_num)

        # new_codes = [3 + 18, ]
        new_codes = []  # TODO: long strings
        for x, y in zip(codes, key_num):
            new_codes.append(x + y)
        # print(new_codes)

        # correct outstanding codes
        very_new_codes = []
        for elem in new_codes:
            if elem > len(self.abc):
                elem -= len(self.abc)
            very_new_codes.append(elem)
        # print(very_new_codes)

        # build the text answer
        result = []
        for code in very_new_codes:  # O(n)
            result.append(self.letter_by_number[code])  # O(1)
        # print(result)
        return ''.join(result)

    def decode(self, text):
        # convert all chars to codes
        if text.isupper():
            return text
        codes = [self.number_by_letter[char] for char in text]
        # print(codes)

        # find new codes for each letter
        key_num = [self.number_by_letter[letter] for letter in self.key]
        # print(key_num)

        # new_codes = [3 + 18, ]
        new_codes = []  # TODO: long strings
        for x, y in zip(codes, key_num):
            new_codes.append(x - y)
        # print(new_codes)

        # correct outstanding codes
        very_new_codes = []
        for elem in new_codes:
            if elem < 0:
                elem += len(self.abc)
            very_new_codes.append(elem)
        # print(very_new_codes)

        # build the text answer
        result = []
        for code in very_new_codes:  # O(n)
            result.append(self.letter_by_number[code])  # O(1)
        # print(result)
        return ''.join(result)


def assert_equals(actual, expected):
    assert actual == expected, f"{actual} is not equeal to {expected}"


def test():
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "password"
    c = VigenereCipher(key, abc)

    assert_equals(c.encode('codewars'), 'rovwsoiv')
    assert_equals(c.decode('rovwsoiv'), 'codewars')

    assert_equals(c.encode('waffles'), 'laxxhsj')
    assert_equals(c.decode('laxxhsj'), 'waffles')

    assert_equals(c.encode('CODEWARS'), 'CODEWARS')
    assert_equals(c.decode('CODEWARS'), 'CODEWARS')

    assert_equals(c.encode('iwantanewshinyferrari'), 'idontknowtherightanswer')


if __name__ == "__main__":
    test()
