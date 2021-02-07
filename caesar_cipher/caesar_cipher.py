import nltk
from nltk.corpus import words

nltk.download("words", quiet=True)
word_list = words.words()


def encrypt(string, shift):
    caesar_string = ""
    if shift > 25 or shift < -25:
        shift = shift % 25
    for character in string:
        if character.isalpha():
            o_num = ord(character)
            character = chr(o_num + shift)
            e_num = ord(character)
            if chr(o_num).isupper():
                if e_num < 65:
                    character = chr((90 + ord(chr(o_num)) + shift) - 65 + 1)
                if e_num > 90:
                    character = chr(65 + ord(chr(o_num)) - 90 + shift - 1)
            if chr(o_num).islower():
                if e_num < 97:
                    character = chr((122 + ord(chr(o_num)) + shift) - 97 + 1)
                if e_num > 122:
                    character = chr(97 + ord(chr(o_num)) - 122 + shift - 1)

        caesar_string += character

    return caesar_string


def decrypt(string, shift):
    original_string = encrypt(string, -shift)
    return original_string


def crack(cypher):
    parsed_cypher = cypher.split(" ")
    cracked_list = []
    for i in range(26):
        cracked_sublist = []
        for word in parsed_cypher:
            shift_word = encrypt(word, i)
            stripped_word = ""
            for character in shift_word:
                if character.isalpha():
                    stripped_word += character.lower()
            if stripped_word in word_list:
                cracked_sublist.append(shift_word)
        cracked_list.append(cracked_sublist)

    index = len(cracked_list)
    longest_sublist = 0
    for i in range(index):
        for j in range(index):
            if len(cracked_list[i]) > longest_sublist:
                longest_sublist = i

    cracked_string = " "
    cracked_string = cracked_string.join(cracked_list[longest_sublist])

    return cracked_string


def eval():
    pass


if __name__ == "__main__":
    test_string = "It was the best of times, it was the worst of times."
    encrypted_test_string = encrypt(test_string, 3)
    print(decrypt(encrypted_test_string, 3))
    print(crack(encrypted_test_string))
