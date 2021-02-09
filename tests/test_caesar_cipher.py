import pytest
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack


def test_encrypt():
    actual = encrypt("Who's #1? YOU'RE #1!", 3)
    expected = "Zkr'v #1? BRX'UH #1!"
    assert actual == expected


def test_decrypt():
    actual = decrypt("Zkr'v #1? BRX'UH #1!", 3)
    expected = "Who's #1? YOU'RE #1!"
    assert actual == expected


def test_crack():
    actual = crack("Lw zdv wkh ehvw ri wlphv, lw zdv wkh zruvw ri wlphv.")
    expected = "It was the best of times, it was the worst of times."
    assert actual == expected
