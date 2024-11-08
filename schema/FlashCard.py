from datetime import date, timedelta
from pydantic import BaseModel
from schema.Level import Level
from typing import Optional


class FlashCard(BaseModel):
    deck_name: str
    question: str
    answer: str
    level: str = Level.RED.value
    seen_on: date = date.today()
    show_again_after: date = seen_on + timedelta(days=0)

    def set_review(self):
        if self.level == Level.RED.value:
            self.show_again_after = date.today() + timedelta(days=1)
        elif self.level == Level.ORANGE:
            self.show_again_after = date.today() + timedelta(days=5)
        else:
            self.show_again_after = date.today() + timedelta(days=10)
# class FlashCard(BaseModel):
# def __init__(self, deck_name: str, question: str, answer: str) -> None:
#     self.deck_name: list[str] = []
#     self.deck_name.append(deck_name)
#     self.question = question
#     self.answer = answer
#     self.level: Level = Level.RED
#     self.seen_on: date = date.today()
#     self.show_again_after: date = self.seen_on + timedelta(days=-1)
#
# def set_review(self):
#     if self.level == Level.RED:
#         self.show_again_after = date.today() + timedelta(days=1)
#     elif self.level == Level.ORANGE:
#         self.show_again_after = date.today() + timedelta(days=5)
#     else:
#         self.show_again_after = date.today() + timedelta(days=10)
