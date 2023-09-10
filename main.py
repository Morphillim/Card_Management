# from cards import build_deck
import sys
from data import check_files
from players import Player

# set max number of possible players to track
max_players = 2


def main():
    # all_decks = []
    print("How many players? ")
    num_players = int(input())

    # stop = False
    if num_players > max_players:
        sys.exit("Unsupported Player Count")

    if check_files(num_players) == 1:
        sys.exit("Not enough files to make cards for all decks;\nCheck if there is a .xlsx file for all decks")

    # for i in range(1, num_players):
    # deck = build_deck(f cards{i}.xlsx')
    players = []
    for i in range(1, num_players + 1):
        player_name = input(f"Name for player {i}? ")
        player = Player(i, player_name)
        players.append(player)
    for i in range(0, len(players)):
        print(players[i].name)


if __name__ == '__main__':
    main()
