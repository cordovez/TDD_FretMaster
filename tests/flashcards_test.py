from schema.Deck import Deck
from schema.FlashCard import FlashCard

test_card1 = FlashCard("person", "What is my name", "Juan Carlos")
test_card2 = FlashCard("person", "What is my last name", "Cordovez")


def create_deck(cards: list[FlashCard], deck_name: str) -> Deck:
    new_deck = Deck(deck_name)
    for deck_card in cards:
        new_deck.cards.append(deck_card)

    return new_deck


def test_should_create_deck() -> None:
    new_deck = create_deck([test_card1, test_card2], "person")
    assert new_deck.deck_name == "person" and len(new_deck.cards) > 0


def test_should_create_flashcard() -> None:
    card = FlashCard("person", "What is my name", "Juan Carlos")
    assert "person" in card.deck and card.question == "What is my name"
