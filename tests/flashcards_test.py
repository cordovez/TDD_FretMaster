import random

from data.all_notes import Fretboard


def test_position_selects_correct_frets():
    fretboard = Fretboard()
    one = fretboard.position_1()
    two = fretboard.position_2()
    three = fretboard.position_3()
    four = fretboard.position_4()
    five = fretboard.position_5()
    six = fretboard.position_6()
    seven = fretboard.position_7()

    print(four)

    assert True

def test_random_choice_is_within_position():
    pass