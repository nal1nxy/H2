"""
File: test_constructor.py
Initial developers: COMP 801 instructors
Developer: Nalin Yetukuri
"""
import pytest
from scrabble_letters import ScrabbleLetters


def test_constructor_1():
    """
    Test the constructor od ScrabbleLetters by giving
      the path of the file as absolute path
    """
    filepath = """C:/Users/Nalin/courses/comp801/Homework
    /h2-NalinYet/scrabble.csv"""
    testfile = ScrabbleLetters(filepath)
    actual = testfile.scrabble_letters
    expected = {'a': [9, 1], 'b': [2, 3], 'c': [2, 3],
                'd': [4, 2], 'e': [12, 1], 'f': [2, 4],
                'g': [3, 2], 'h': [2, 4], 'i': [9, 1],
                'j': [1, 8], 'k': [1, 5], 'l': [4, 1],
                'm': [2, 3], 'n': [6, 1], 'o': [8, 1],
                'p': [2, 3], 'q': [1, 10], 'r': [6, 1],
                's': [4, 1], 't': [6, 1], 'u': [4, 1],
                'v': [2, 4], 'w': [2, 4], 'x': [1, 8],
                'y': [2, 4], 'z': [1, 10], ' ': [2, 0]}
    assert actual == expected


def test_constructor_2():
    """
    Test the constructor of ScrabbleLetters by accessing the file directly
     using it's file name
    """
    filepath = "scrabble.csv"
    testfile = ScrabbleLetters(filepath)
    actual = testfile.scrabble_letters
    expected = {'a': [9, 1], 'b': [2, 3], 'c': [2, 3],
                'd': [4, 2], 'e': [12, 1], 'f': [2, 4],
                'g': [3, 2], 'h': [2, 4], 'i': [9, 1],
                'j': [1, 8], 'k': [1, 5], 'l': [4, 1],
                'm': [2, 3], 'n': [6, 1], 'o': [8, 1],
                'p': [2, 3], 'q': [1, 10], 'r': [6, 1],
                's': [4, 1], 't': [6, 1], 'u': [4, 1],
                'v': [2, 4], 'w': [2, 4], 'x': [1, 8],
                'y': [2, 4], 'z': [1, 10], ' ': [2, 0]}
    assert actual == expected


pytest.main()
