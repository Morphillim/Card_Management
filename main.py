# from cards import build_deck
import sys
from data import check_files

# set max number of possible players to track
max_players = 2


def main():
    # all_decks = []
    print("How many decks? (1 or 2)\n")
    number_decks = int(input())
    num_players = number_decks

    # stop = False
    if num_players > max_players:
        sys.exit("Unsupported Player Count")

    if check_files(num_players) != 0:
        sys.exit("Not enough files to make cards for all decks;\nCheck if there is a .xlsx file for all decks")

    # for i in range(1, num_players):
    # deck = build_deck(f cards{i}.xlsx')
    # players = []


if __name__ == '__main__':
    main()
