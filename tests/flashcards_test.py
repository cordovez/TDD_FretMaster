from data import all_notes
from helpers.create_decks import create_deck, fretboard_deck
from schema.FlashCard import FlashCard

test_card1 = FlashCard("person", "What is my name", "Juan Carlos")
test_card2 = FlashCard("person", "What is my last name", "Cordovez")

class TestCreateDecks:
    def test_should_create_deck(self) -> None:
        new_deck = create_deck([test_card1, test_card2], "person")
        assert new_deck.deck_name == "person" and len(new_deck.cards) > 0

    def test_should_create_flashcard(self) -> None:
        card = FlashCard("person", "What is my name", "Juan Carlos")
        assert "person" in card.deck and card.question == "What is my name"

    def test_should_create_deck_for_all_fretboard(self) -> None:
        fretboard = all_notes.fretboard
        number_of_frets: int = len(fretboard)
        strings_on_guitar: int = 6
        number_of_notes: int = number_of_frets * strings_on_guitar

        new_deck = fretboard_deck(fretboard)
        assert len(new_deck) == number_of_notes




