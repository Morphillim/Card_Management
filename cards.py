from openpyxl import load_workbook
# import random
from enum import Enum


def build_deck(path):
    workbook = load_workbook(filename=path)
    sheet = workbook.active
    rows = 0
    col = 'A'
    temp_deck = []

    for cell in sheet[col]:
        if cell.value is None:
            break
        else:
            rows += 1
    for j in range(1, rows):
        name = None
        tier = None
        value = None
        metric = None
        vitality = None
        ability = None
        text = None

        for cell in sheet[j]:
            if cell.value is None:
                break
            else:
                if cell.column == 1:
                    name = cell.value
                elif cell.column == 2:
                    tier = cell.value
                elif cell.column == 3:
                    value = cell.value
                elif cell.column == 4:
                    metric = cell.value
                elif cell.column == 5:
                    vitality = cell.value
                elif cell.column == 6:
                    ability = cell.value
                elif cell.column == 7:
                    text = cell.value
                else:
                    continue
        card = Card(name, tier, value, metric, vitality, ability, text)
        # print(card.name)
        temp_deck.append(card)
    return temp_deck


class Card:
    name = None
    tier = None
    value = None
    metric = None
    vitality = None
    ability = None
    text = None

    def __init__(self, name, tier, value, metric, vitality, ability, text):
        self.name = name
        self.tier = tier
        self.value = value
        self.metric = metric
        self.vitality = vitality
        self.ability = ability
        self.text = text

    def print(self):
        # print(f"Details of {self.name}")
        print(f'Name: {self.name}\nTier: {Tier(self.tier).name}\nValue: {self.value}\nMetric: {self.metric}\nVitality: '
              f'{self.vitality}\nAbility: {self.ability}\nText: {self.text}\n')

    def print_stat(self, stat):
        if stat == "name":
            print(f'Name: {self.name}')
        elif stat == "tier":
            print(f'Tier: {Tier(self.tier).name}')
        elif stat == "value":
            print(f'Value: {self.value}')
        elif stat == "metric":
            print(f'Metric: {self.metric}')
        elif stat == "vitality":
            print(f'Vitality: {self.vitality}')
        elif stat == "ability":
            print(f'Ability: {self.ability}')
        elif stat == "text":
            print(f'Text: {self.text}')
        else:
            print("Invalid Stat")


class Tier(Enum):
    Spell = 0
    Resource = 1
    Lesser_Creature = 2
    Greater_Creature = 3
    Special = 4
    Monstrosity = 5


class Costs(Enum):
    Free = 0
    Resources = 1
    Force = 2
    Sacrifice = 3
