from classes2048 import Game2048
from classes2048 import Direction
# TUI STANDS FOR 'TEXT USER INTERFACE'

'''
This file runs a text user interface for the game 2048. A user types commands
to play the game according to the instructions printed to standard output
when the game starts.

When the game is over, the code stops running and the users score is displayed
to standard output.
'''

# BELOW ARE THE WELCOME INSTRUCTIONS WHEN A USER RUNS THE TUI
print("\nWELCOME TO 2048!!!!\n")
print("To move you have a few options...")
print("You can play by using the 'W', 'A', 'S', and 'D' keys (gamer style!)\n")
print("Input 'w' to move up")
print("Input 'a' to move left")
print("Input 'a' to move down")
print("Input 'a' to move right\n")
print("You can also input 'AI' to have my code suggest a move for you.\n")
print("WARNING: The AI assumes the user has stacked it's largest")
print("tiles on the bottom of the board, as this kind of approach")
print("is one of the most common strategies.\n")
print("The AI is pretty powerful, but the moves it suggests only win")
print("about one in four games so don't rely on it too much...\n")

game = Game2048()
is_game_won = False

# game starts with two pieces on the board
game.add_random_piece(game.board)
game.add_random_piece(game.board)

# continules to ask for user input until game is over or user quits after 
# winning
while not game.is_game_over():
    move = None

    print("Score:", game.score)
    game.show_board(game.board)

    if not is_game_won and game.is_game_won():
        is_game_won = True
        print("Congrats!!!!! You Won!!!")
        print("To continue press 'y'. To quit press 'n'.")
        will_continue = input("Continue? y/n: ")
        if will_continue == 'y':
            will_continue_bool = True
        else:
            will_continue_bool = False
        
        if not will_continue_bool:
            break

    move_str = input("Type a direction: ").upper()
    print()
    if move_str == "A":
        move = Direction.LEFT
    elif move_str == "D":
        move = Direction.RIGHT
    elif move_str == "S":
        move = Direction.DOWN
    elif move_str == "W":
        move = Direction.UP
    elif move_str == "AI":
        move = game.suggest_move()
    else:
        print("Enter a valid move for the given board:")
    
    if not game.is_move_possible(move, game.board):
        print("Enter a valid move for the given board:")
        move = None

    if move != None:
        game.move(move, game.board)

game.show_board(game.board)

print("GAME OVER")
print("Your score was", game.score)

