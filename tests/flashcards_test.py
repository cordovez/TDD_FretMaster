from data import all_notes
from helpers.c_key import create_key_of_c_deck
from helpers.create_decks import create_deck, create_deck_with_name
from schema.Deck import Deck
from schema.FlashCard import FlashCard

test_card1 = FlashCard(deck_name="person", question="What is my name",
                       answer="Juan Carlos")
test_card2 = FlashCard(deck_name="person", question="What is my last name",
                       answer="Cordovez")


class TestCreateDecks:
    def test_should_create_deck(self) -> None:
        new_deck = create_deck([test_card1, test_card2], "person")
        assert new_deck.deck_name == "person" and len(new_deck.cards) > 0

    def test_should_create_flashcard(self) -> None:
        card = FlashCard(deck_name="person", question="What is my name", answer="Juan "
                                                                                "Carlos")
        assert card.deck_name == "person" and card.question == "What is my name"

    def test_should_create_deck_for_all_fretboard(self) -> None:
        fretboard = all_notes.fretboard
        number_of_frets: int = len(fretboard)
        strings_on_guitar: int = 6
        number_of_notes: int = number_of_frets * strings_on_guitar

        new_deck: Deck = create_deck_with_name(name="whole_fretboard", data=fretboard)
        assert len(new_deck) == number_of_notes


class TestPositions:
    def test_should_return_key_of_c_fourth_position(self) -> None:
        notes = create_key_of_c_deck()
        assert notes[0]["deck_name"] == "key_of_c"

        # print([(card.question, card.answer) for card in key_of_c])
        # return new_deck
