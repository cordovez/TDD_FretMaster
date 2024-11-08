import json

from data import all_notes
from data.all_notes import Fretboard
from helpers.create_decks import create_deck_with_name
from pathlib import Path

from schema.FlashCard import FlashCard


def save_deck_to_db(deck: list) -> None:
    file_path = Path(__file__).resolve().parent.parent / "data" / "c_04.py"

    with file_path.open("w") as f:
        f.write(f"key_of_c = {deck}")


def create_key_of_c_complete() -> list[FlashCard]:
    fretboard = all_notes.complete
    new_deck = create_deck_with_name("key_of_c", fretboard)
    key_of_c = [card.model_dump() for card in new_deck if "b" not in card.answer]

    save_deck_to_db(key_of_c)

    return key_of_c


if __name__ == '__main__':
    fret = Fretboard()
    print(fret.position_4())
