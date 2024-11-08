from schema.Deck import Deck
from schema.FlashCard import FlashCard


def create_deck(cards: list[FlashCard], deck_name: str) -> Deck:
    new_deck = Deck(deck_name=deck_name)
    for deck_card in cards:
        new_deck.cards.append(deck_card)

    return new_deck


def create_deck_with_name(name: str, data: list) -> Deck:
    new_deck: Deck = []
    for fret in data:
        for string in fret:
            for k, v in string.items():
                card = FlashCard(deck_name=name, question=k, answer=v)
                new_deck.append(card)
    return new_deck
