from schema.Deck import Deck
from schema.FlashCard import FlashCard


def create_deck(cards: list[FlashCard], deck_name: str) -> Deck:
    new_deck = Deck(deck_name)
    for deck_card in cards:
        new_deck.cards.append(deck_card)

    return new_deck


def fretboard_deck(data):
    new_deck = []
    for fret in data:
        for string in fret:
            for k, v in string.items():
                card = FlashCard("fretboard", k, v)
                new_deck.append(card)
    return new_deck
