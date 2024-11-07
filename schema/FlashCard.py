from datetime import date, timedelta

from schema.Level import Level


class FlashCard:
    def __init__(self, deck_name: str, question: str, answer: str) -> None:
        self.deck: list[str] = []
        self.deck.append(deck_name)
        self.question = question
        self.answer = answer
        self.level: Level = Level.RED
        self.seen_on: date = date.today()
        self.show_again_after: date = self.seen_on + timedelta(days=-1)

    def set_review(self):
        if self.level == Level.RED:
            self.show_again_after = date.today() + timedelta(days=1)
        elif self.level == Level.ORANGE:
            self.show_again_after = date.today() + timedelta(days=5)
        else:
            self.show_again_after = date.today() + timedelta(days=10)
