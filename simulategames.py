from classes2048 import Game2048
NUM_GAMES = 1000
'''
File simulates 1000 games of 2048 where each move is suggested by the
"suggest move" method in the Game2048 class.

After the 1000 games are simulated, information about the games played is 
printed to standard output:
    1. The number of games played
    2. The number of wins
    3. The number of wins greater than 2048
    4. The top tile from all the games
    5. The percentage of wins
'''

def num_wins(top_tiles):
    '''
    Takes a last of top tiles and returns the number of them that are
    2048 or greater

    Perameters:
        top_tiles (list of int): The top value of tiles from each game played
    
    Returns:
        count_2048 (int): Number of games where the top tile was 2048 or greater
    '''
    count_2048 = 0
    for tile in top_tiles:
        if tile >= 2048:
            count_2048 += 1
    
    return (count_2048)

def wins_greater_than_2048(top_tiles):
    '''
    Takes a list of top tiles and returns the number of tiles that are
    greater than 2048.

    Perameters:
        top_tiles (list of int): The top value of tiles from each game played
    
    Returns:
        count_2048 (int): Number of games where the top tile was greater than 2048
    '''
    rv = []
    for tile in top_tiles:
        if tile > 2048:
            rv.append(tile)
    return rv

top_tiles = []

for i in range(NUM_GAMES):
    game = Game2048()

    # Game starts with two pieces on the board
    game.add_random_piece(game.board)
    game.add_random_piece(game.board)

    while not game.is_game_over():
        game.move(game.suggest_move(), game.board)
    
    largest_piece = game.get_largest_piece()
    top_tiles.append(largest_piece)

num_wins = num_wins(top_tiles)

print("Output:")
print("Number of games played:", NUM_GAMES)
print("Number of wins:", num_wins)
print("Number of wins greater than 2048:", len(wins_greater_than_2048(top_tiles)))
print("Top tile", max(top_tiles))
print("Percentage of wins", str((num_wins / NUM_GAMES) * 100) + "%")

