"""
File: test_get_freq.py
Initial developers: COMP 801 instructors
Developer: Nalin Yetukuri
"""

import pytest
from scrabble_letters import ScrabbleLetters


def test_get_freq_1():
    """
    Test the method by giving a word with a blank space as input
    """
    word = "a c"
    test_word = ScrabbleLetters("scrabble.csv")
    actual = test_word.get_freq(word)
    expected = {"a": 9, " ": 2, "c": 2}
    assert actual == expected


def test_get_freq_2():
    """
    test the method by giving a word with letters in upper case
    """
    word = "ABC"
    test_word = ScrabbleLetters("scrabble.csv")
    actual = test_word.get_freq(word)
    expected = {"a": 9, "b": 2, "c": 2}
    assert actual == expected


pytest.main()
