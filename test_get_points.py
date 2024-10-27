"""
File: test_get_points.py
Initial developers: COMP 801 instructors
Developer: Nalin Yetukuri
"""

import pytest
from scrabble_letters import ScrabbleLetters


def test_get_points_1():
    """
    Test the method by giving a word with uppercase letters as input
    """
    word = "HACK"
    test_word = ScrabbleLetters("scrabble.csv")
    actual = test_word.get_points(word)
    expected = 13
    assert actual == expected


def test_get_points_2():
    """
    Test the method by giving a word with blank spaces in it as input
    """
    word = "h A cK"
    test_word = ScrabbleLetters("scrabble.csv")
    actual = test_word.get_points(word)
    expected = 13
    assert actual == expected


pytest.main()
