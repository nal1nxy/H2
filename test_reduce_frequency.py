"""
File: test_reduce_frequency.py
Initial developers: COMP 801 instructors
Developer: Nalin Yetukuri
"""
import pytest
from scrabble_letters import ScrabbleLetters


def test_reduce_frequency_1():
    """
    Test the method by giving an uppercase letter as input
    """
    letter = "E"
    test_letter = ScrabbleLetters(letter)
    actual = test_letter.reduce_freqeuncy(letter)
    expected = True
    assert actual == expected


def test_reduce_frequency_2():
    """
    Test the method by giving the string "blank" as input
    """
    letter = "blank"
    test_letter = ScrabbleLetters(letter)
    actual = test_letter.reduce_freqeuncy(letter)
    expected = True
    assert actual == expected


pytest.main()
