# from cards import build_deck
import sys
from data import check_files
from players import Player

# set max number of possible players to track
max_players = 2

# curr_player = 0

def pick(currplayer, num):
    print(f'{currplayer} {num}')


def next_player(player, num, max):
    if player <= 0:
        next = max - 1
    elif player == max - 1:
        next = 0
    elif num > 1:
        next = player + 1
    else:
        next = num
    return next



def main():
    options = ("   0. Quit                      1. Draw\n"
               "   2. Read Hand                 3. Place Card\n"
               "   4. Field to discard          5. Field to hand\n"
               "   6. Hand to discard           7. Read Field\n"
               "   8. Next Player")
    # all_decks = []
    # print("How many players? ")
    num_players = int(input("How many players? "))
    curr_player = 0

    stop = False
    if num_players > max_players or num_players <= 0:
        sys.exit("Unsupported Player Count")

    if check_files(num_players) == 1:
        sys.exit("Not enough files to make cards for all decks;\nCheck if there is a .xlsx file for all decks")

    # for i in range(1, num_players):
    # deck = build_deck(f cards{i}.xlsx')
    players = []
    for i in range(1, num_players + 1):
        player = Player(i, input(f"Name for player {i}? "))
        players.append(player)
    # for i in range(0, len(players)):
    #    print(f'Player {players[i].name}')
    #    for j in range(0, len(players[i].deck)):
    #        players[i].deck[j].print()
    go = True
    while go:
        tmp_input = ""
        # choices = [sys.exit("Quiting Program"), players[curr_player].read_hand()]
        print(f"player {curr_player}\nOptions:")
        print(options)
        userInput = int(input(" > "))
        if userInput == 0:
            go = False
        elif userInput == 1:
            players[curr_player].draw(1)
        elif userInput == 2:
            players[curr_player].read_hand()
        elif userInput == 3:
            tmp_input = input("Enter name of card to place: ")
            players[curr_player].hand_field(tmp_input)
        elif userInput == 4:
            tmp_input = input("Enter name of card going from field to discard: ")
            players[curr_player].field_discard(tmp_input)
        elif userInput == 5:
            tmp_input = input("Enter name of card to move from field to hand: ")
            players[curr_player].field_hand(tmp_input)
        elif userInput == 6:
            tmp_input = input("Enter name of card to discard from hand: ")
            players[curr_player].discard(tmp_input)
        elif userInput == 7:
            players[curr_player].read_field()
        elif userInput == 8:
            curr_player = next_player(curr_player, num_players, max_players)
        print("======================")



if __name__ == '__main__':
    main()
