from cards import build_deck
import random


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
        random.shuffle(self.deck)
        self.draw(7)

    # def read_stats(self):
    #     for i in (0, len(self.deck)):
    #         self.draw_pile[i].print()
    def shuffle_draw(self):
        random.shuffle(self.draw_pile)

    def draw(self, num):
        for i in range(0, num):
            self.hand.append(self.draw_pile[i])
        for i in range(0, num):
            self.draw_pile.pop(i)

    def discard_from_hand(self, removals):
        for i in range(0, len(removals)):
            self.discard_pile.append(removals[i])
        for i in range(0, len(removals)):
            self.hand.remove(removals[i].name)

    def discard(self, name):
        for i in range(0, len(self.hand)):
            if self.hand[i].name == name:
                self.discard_pile.append(self.hand[i])
                self.hand.pop(i)

    def clear_hand(self):
        for i in range(0, len(self.hand)):
            self.discard_pile.append(self.hand[i])
        for i in range(0, len(self.hand)):
            self.hand.clear()

    def reshuffle_draw(self):
        self.clear_hand()
        for i in range(0, len(self.discard_pile)):
            self.draw_pile.append(self.discard_pile[i])
        for i in range(0, len(self.discard_pile)):
            self.discard_pile.clear()
        self.shuffle_draw()

    def read_hand(self):
        if len(self.hand) == 0:
            print("Hand Empty")
        else:
            for i in range(0, len(self.hand)):
                self.hand[i].print()

    def read_field(self):
        if len(self.field) == 0:
            print("Field Empty")
        else:
            for i in range(0, len(self.field)):
                self.field[i].print()

    def field_hand(self, name):
        for i in range(0, len(self.field)):
            if self.field[i].name == name:
                self.hand.append(self.field[i])
                self.field.pop(i)
                break

    def hand_field(self, name):
        for i in range(0, len(self.hand)):
            if self.hand[i].name == name:
                self.field.append(self.hand[i])
                self.hand.pop(i)
                break

    def field_discard(self, name):
        for i in range(0, len(self.field)):
            if self.field[i].name == name:
                self.discard_pile.append(self.field[i])
                self.field.pop(i)
                break
