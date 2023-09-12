# Card_Management

Card_Management is a program that virtualizes how cards in the game Antimony are handled during use.

# Usage

## Prep

First, create a spreadsheet to represent the decks for each player you plan to use; this will be in the form of a .xlsx, placed in a \decks subdirectory.

In each workbook, formating goes as follows:
Each row represents a card in the deck. The number of rows you fill represents the number of cards that will be in your deck.
Each column represents a card detail, in the Order of name, tier, value, metric, vitality, ability, and text.

If you wish to represent more than 2 players, change the max_players vairable in the main.py file.

## Using

After launchng the main.py file, the user will be prompted to enter the number of players, then name each player.

The program then enters a prompt loop where the user will be prompted to choose between interacting with the current player's cards, to switch to the next player, or to quit the program.
