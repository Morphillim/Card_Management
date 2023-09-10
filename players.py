from cards import build_deck


class Player:
    name = "player"
    deck = None
    draw_pile = None
    discard_pile = []
    hand = []
    field = []

    def __init__(self, num, name):
        self.name = name
        self.deck = build_deck(f'decks\\cards{num}.xlsx')
        self.draw_pile = self.deck
