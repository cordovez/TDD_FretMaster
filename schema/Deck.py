from schema.FlashCard import FlashCard
from schema.Level import Level


class Deck:
    def __init__(self, deck_name: str):
        self.level: Level = Level.RED
        self.deck_name = deck_name
        self.cards: list[FlashCard] = []
