from schema.FlashCard import FlashCard
from schema.Level import Level
from pydantic import BaseModel


class Deck(BaseModel):
    deck_name: str
    level: str = Level.RED.value
    cards: list[FlashCard] = []
