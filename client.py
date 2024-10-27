"""
Practice with the dictionary built-in data type
and file reading.

File: client.py
Initial developers: COMP 801 instructors
Developer: Nalin
"""
from scrabble_letters import ScrabbleLetters


def main():
    """
    Demo ScrabbleLetters functionality
    """

    letters_file = "scrabble.csv"

    scrabble = ScrabbleLetters(letters_file)
    print(scrabble.scrabble_letters)
    letter = " "
    print(scrabble.reduce_freqeuncy(letter))
    print(scrabble.reduce_freqeuncy(letter))
    letters = "ABC"
    print(scrabble.get_freq(letters))


def easy():
    """
    Read the content of the file using readline().
    """
    easy_file = "sample.txt"

    with open(file=easy_file, encoding='UTF-8', mode='r') as file_object:

        line = file_object.readline()

    while line:
        line = line.strip()
        print(line)
        line = file_object.readline()


def other():
    """
    Read the content of the file iterating throught the file object directly.
    """
    #


if __name__ == "__main__":
    main()
    other()
