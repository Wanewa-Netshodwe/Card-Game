# Terminal-Based Card Game README
This README provides instructions for a Python-based, terminal card game inspired by Uno. It features action cards like "Reverse," "Skip," and "Draw," along with a special rule where the "Reverse" card causes players to swap their hands.

## Game Overview
In this two-player, turn-based game, a human and computer take turns playing cards that match the color or number of the top card in the discard pile. The objective is to be the first to get rid of all cards in hand. The game includes action cards with the following effects:

- Skip: Skips the opponent’s turn.
- Draw: Forces the opponent to draw two cards.
- Reverse: Causes both players to swap hands.
## Features
1. Player Actions: Players must either play a card that matches the discard pile's top card by color or number or draw a new card if no match is available.
2. Special Cards:
   - Skip: Skips the next player's turn.
   - Draw: Makes the next player draw two cards.
   - Reverse: Swaps hands between players.
Win Condition: The first player to empty their hand wins.
## Setup and Rules
- Deck: Generated with four colors (Blue, Green, Yellow, Red), and includes numbers 1-9 plus action cards (Skip, Draw, Reverse).
- Players: The human player and computer each start with 7 randomly drawn cards.
- Starting the Game: The game begins by placing one card in the discard pile, and players then take turns in a terminal-based interaction.
## Game Structure
- Game Loop: The game continues in a loop until a player wins by emptying their hand.
- Human Player's Move: Prompted to either play a card by selecting its index or draw a card if no matching card is available.
- Computer's Move: Automatically selects a playable card or draws if needed.
- Special Rules: Playing a "Reverse" card swaps hands, adding a unique challenge.
## Code Functions
1. handoutCards(): Distributes initial cards to each player.
2. isSpecialCard(card): Checks if a card is an action card.
3. draw(p): Adds two cards to the opponent’s hand when a Draw card is played.
4. reverse(): Swaps the hands of both players when a Reverse card is played.
5. make_move(p): Handles turn logic for both human and computer players, providing prompts and managing actions.
6. gameStart(gameover): Initializes and runs the game loop until a player wins.
## How to Play
- Run the Code: Start the game in your terminal.
- Human Player’s Turn: Enter "D" to draw a card, or input the index of a card to play if it matches the color or number of the discard pile's top card.
C- omputer’s Turn: The computer will play automatically, attempting to match the top discard card.
S- pecial Cards: Trigger actions like skipping turns, forcing draws, or swapping hands.
- Winning: The game ends when a player has no cards left and is declared the winner.
## Notes
The terminal interface guides human player actions.
The computer’s moves simulate turn-taking with pauses for realism.
## Dependencies
random: For deck shuffling.
time.sleep: For simulating the computer's actions with delays.
## Improvements
Future development could expand to support multiple players, include wild cards, and add more interactive features.

Enjoy the game, and good luck!
