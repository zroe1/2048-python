from enum import Enum
import random
import logging
import itertools

Direction = Enum('Direction', ['LEFT', 'RIGHT', 'UP', 'DOWN'])
Combination_Direction = Enum('Combination_Direction', ['Horizontal', 'Vertical'])
Board_Section = Enum('Board_Section', ['bottom_l, bottom_r, top_l, top_r'])

class Game2048:
    def __init__(self):
        '''
        Creates a game of 2048
        '''
        self.score = 0
        self.last_move_up = False
        self.board = [[None, None, None, None],
                      [None, None, None, None],
                      [None, None, None, None],
                      [None, None, None, None]]

    def is_game_won(self):
        '''
        Checks if there is a 2048 tile on the board. If there is, function
        returns true because that means player won the game.

        Returns:
            (boolean): True if game is won, false otherwise
        '''
        for row in self.board:
            for num in row:
                if num == 2048:
                    return True
        
        return False

    def get_largest_piece(self):
        '''
        Returns the value of the largest piece on the board.

        Returns:
            max (int): The value of the largest tile.
        '''
        max = 0
        for row in self.board:
            for num in row:
                if num != None and num > max:
                    max = num
        return max
    
    def loc_largest_piece(self, board):
        '''
        Returns the location of the largest peice on the board.

        Perameters:
            board (list of list): 2048 board the function searches

        Returns:
            max_loc (tuple: (int, int)): The location of largest piece (row, col)
        '''
        max = 0
        max_loc = None
        for i in range(4):
            for j in range(4):
                if board[i][j] != None and board[i][j] > max:
                    max =  board[i][j]
                    max_loc = (i, j)
        return max_loc

    def is_game_over(self):
        '''
        Checks if the game is over (meaning there are no empty spaces on the
        board).

        Returns:
            (boolean): True if game is over, False otherwise.
        '''
        return not (self.is_down_possible(self.board) or self.is_up_possible(self.board) or
            self.is_left_possible(self.board) or self.is_right_possible(self.board))

    def space_open(self, loc, board):
        '''
        Returns true if given space on the board is None

        Perameters:
            loc (tuple: (int, int)): location to check (row, col)
            board (list of list): 2048 board the function searches

        Returns:
            (boolean): True if the space is open (None), False otherwise
        '''
        return board[loc[0]][loc[1]] == None

    def add_piece(self, piece_num, loc, board):
        '''
        Adds a piece with the value piece_num to a location loc on the
        board

        Perameters:
            piece_num (int): value of piece to be added
            loc (tuple (int, int)): location for piece to be added (row, col)
            board (list of list): 2048 board for piece to be added     
        '''
        if (self.space_open(loc, board)):
            board[loc[0]][loc[1]] = piece_num
        else:
            logging.error('PIECE REPLACED. UNPREDICTABLE BEHAVIOR TO FOLLOW.')

    def add_random_piece(self, board):
        '''
        Adds a random piece to the board passed as a perameter. There is
        a 10% chance that the number added is a four and a 90% chance the
        number added is a two.

        Perameters:
            board (list of list): 2048 board for piece to be added to
        '''
        row_num = random.randint(0,3)
        col_num = random.randint(0,3)

        if (not self.space_open((row_num, col_num), board)):
            return self.add_random_piece(board)

        is_four = random.randint(1,10) ==  1
        if is_four:
            self.add_piece(4, (row_num, col_num), board)
        else:
            self.add_piece(2, (row_num, col_num), board)

    def piece_swap(self, loc1, loc2, board):
        '''
        Swaps two pieces on the board, even if one of those peices is
        None.

        Perameters:
            loc1 (tuple (int, int)): location of first tile to be swapped (row, col)
            loc2 (tuple (int, int)): location of second tile to be swapped (row, col)
            board (list of list): 2048 board where swap occurs
        '''
        temp = board[loc1[0]][loc1[1]]
        board[loc1[0]][loc1[1]] = board[loc2[0]][loc2[1]]
        board[loc2[0]][loc2[1]] = temp

    def combine_pieces(self, loc1, loc2, end_loc, board):
        '''
        Takes the sum of two pieces on the board at loc1 and loc2
        and then sets the values at loc1 and loc2 to None. Finally
        adds the previously calculated sum as a piece at end_loc.

        Perameters:
            loc1 (tuple (int, int)): location of first tile to be combined (row, col)
            loc2 (tuple (int, int)): location of second tile to be combined (row, col)
            end_loc (tuple (int, int)): where the new tile is inserted (row, col)
            board (list of list): 2048 board where combination occurs
        '''
        sum = board[loc1[0]][loc1[1]] + board[loc2[0]][loc2[1]]
        board[loc1[0]][loc1[1]] = None
        board[loc2[0]][loc2[1]] = None
        board[end_loc[0]][end_loc[1]] = sum
        self.score += sum

    def move_up(self, board):
        '''
        Changes game state according to the rules of the game,
        when a user moves up.

        Perameters:
            board (list of list): 2048 board that move occurs on
        '''
        self.shift_pieces_up(board)

        self.move_up_col(0, board)
        self.move_up_col(1, board)
        self.move_up_col(2, board)
        self.move_up_col(3, board)

        self.shift_pieces_up(board)
        self.add_random_piece(board)

    def move_down(self, board):
        '''
        Changes game state according to the rules of the game,
        when a user moves down.

        Perameters:
            board (list of list): 2048 board that move occurs on
        '''
        self.shift_pieces_down(board)

        self.move_down_col(0, board)
        self.move_down_col(1, board)
        self.move_down_col(2, board)
        self.move_down_col(3, board)

        self.shift_pieces_down(board)
        self.add_random_piece(board)

    def move_left(self, board):
        '''
        Changes game state according to the rules of the game,
        when a user moves left.

        Perameters:
            board (list of list): 2048 board that move occurs on
        '''
        self.shift_pieces_left(board)

        self.move_left_row(0, board)
        self.move_left_row(1, board)
        self.move_left_row(2, board)
        self.move_left_row(3, board)
        
        self.shift_pieces_left(board)
        self.add_random_piece(board)

    def move_right(self, board):
        '''
        Changes game state according to the rules of the game,
        when a user moves right.

        Perameters:
            board (list of list): 2048 board that move occurs on
        '''
        self.shift_pieces_right(board)

        self.move_right_row(0, board)
        self.move_right_row(1, board)
        self.move_right_row(2, board)
        self.move_right_row(3, board)

        self.shift_pieces_right(board)
        self.add_random_piece(board)
    
    def shift_pieces_down(self, board):
        '''
        Shifts all game pieces down, meaning that there is no piece on the
        board where the tile below it is None.

        Perameters:
            board (list of list): 2048 board that shift occurs on
        '''
        for col in range(4):
            for iteration in range(3):
                    for row in range(3):
                        if board[row][col] != None and board[row + 1][col] == None:
                            self.piece_swap((row, col), (row + 1, col), board)

    def shift_pieces_up(self, board):
        '''
        Shifts all game pieces down, meaning that there is no piece on the
        board where the tile above it is None.

        Perameters:
            board (list of list): 2048 board that shift occurs on
        '''
        for col in range(4):
            for iteration in range(3):
                for row in range(3):
                    if board[row][col] == None and board[row + 1][col] != None:
                        self.piece_swap((row, col), (row + 1, col), board)

    def shift_pieces_left(self, board):
        '''
        Shifts all game pieces down, meaning that there is no piece on the
        board where the tile to the left of it is None.

        Perameters:
            board (list of list): 2048 board that shift occurs on
        '''
        for row in range(4):
            for iteration in range(3):
                for col in range(3):
                    if board[row][col] == None and board[row][col + 1] != None:
                        self.piece_swap((row, col), (row, col + 1), board)

    def shift_pieces_right(self, board):
        '''
        Shifts all game pieces down, meaning that there is no piece on the
        board where the tile to the right of it is None.

        Perameters:
            board (list of list): 2048 board that shift occurs on
        '''
        for row in range(4):
            for iteration in range(3):
                for col in range(3):
                    if board[row][col] != None and board[row][col + 1] == None:
                        self.piece_swap((row, col), (row, col + 1), board)


    def move_down_col(self, col, board):
        '''
        Combines pieces for a given column according to the properties of a
        down move in 2048. Other elements of the down move are handled by the
        "move_down" method.

        Perameters:
            col (int): The index of the column that the function opperates on
            board (list of list): 2048 board that function opperates on
        '''
        row = 3
        while row > 0:
            piece_above = board[row - 1][col]
            currect_piece = board[row][col]
            if currect_piece != None:
                if piece_above == currect_piece:
                    self.combine_pieces((row, col), (row - 1, col), (row, col), board)   
                    row -= 1
            row -= 1


    def move_up_col(self, col, board):
        '''
        Combines pieces for a given column according to the properties of a
        up move in 2048. Other elements of the down move are handled by the
        "move_up" method.

        Perameters:
            col (int): The index of the column that the function opperates on
            board (list of list): 2048 board that function opperates on
        '''
        row = 0
        while row < 3:
            piece_below = board[row + 1][col]
            current_piece = board[row][col]
            if current_piece != None:
                if piece_below == current_piece:
                    self.combine_pieces((row, col), (row + 1, col), (row, col), board)
                    row += 1
            row += 1

    def move_left_row(self, row, board):
        '''
        Combines pieces for a given row according to the properties of a
        left move in 2048. Other elements of the down move are handled by the
        "move_left" method.

        Perameters:
            row (int): The index of the row that the function opperates on
            board (list of list): 2048 board that function opperates on
        '''
        col = 0
        while col < 3:
            piece_right = board[row][col + 1]
            current_piece = board[row][col]
            
            if current_piece != None:
                if piece_right == board[row][col]:
                    self.combine_pieces((row, col), (row, col + 1), (row, col), board)
                    col += 1
            col += 1

    def move_right_row(self, row, board):
        '''
        Combines pieces for a given row according to the properties of a
        right move in 2048. Other elements of the down move are handled by the
        "move_right" method.

        Perameters:
            row (int): The index of the row that the function opperates on
            board (list of list): 2048 board that function opperates on
        '''
        col = 3
        while col > 0:
            piece_left = board[row][col - 1]
            current_piece = board[row][col]
            
            if current_piece != None:
                if piece_left == board[row][col]:
                    self.combine_pieces((row, col), (row, col - 1), (row, col), board)
                    col -= 1
            col -= 1

    def move(self, direction, board):
        '''
        For a given direction, the function makes a move according to the
        rules of 2048. Assumes that a given move is possible.

        Perameters:
            direction (Enum (Direction)): Direction function makes the move for.
            board (list of list): 2048 board the function makes the move on.
        '''
        if direction == Direction.UP:
            self.move_up(board)
        elif direction == Direction.DOWN:
            self.move_down(board)
        elif direction == Direction.LEFT:
            self.move_left(board)
        else:
            self.move_right(board)

    def is_move_possible(self, direction, board):
        '''
        For a given direction, returns True if the proposed move is possible,
        False otherwise. Assumes user passes valid direction.

        Perameters:
            direction (Enum (Direction)): Direction function checks for legality
            board (list of list): 2048 board the function checks for.

        Returns:
            (boolean): True if the move is legal, false otherwise.
        '''
        if direction == Direction.LEFT:
            return self.is_left_possible(board)
        elif direction == Direction.RIGHT:
            return self.is_right_possible(board)
        elif direction == Direction.DOWN:
            return self.is_down_possible(board)
        else:
            return self.is_up_possible(board)
    
    def max_tile_position(self):
        '''
        Returns the position of the largest tile on the board.

        Returns:
            (tuple: (int, int)): position of the largest tile (row, col)
        '''
        max = 0
        max_position = (3, 3)

        for i in range(4):
            for j in range(4):
                if self.board[i][j] != None and max < self.board[i][j]:
                    max = self.board[i][j]
                    max_position = (i, j)
        return max_position

    def is_right_possible(self, board):
        '''
        Returns true if right move is possible, False otherwise.

        Perameters:
            board (list of list): 2048 board the function checks for.

        Returns:
            (boolean): True if move is legal, false otherwise
        '''
        for i in range(4):
            for j in range(3):
                if (board[i][j] != None and (board[i][j + 1] == None
                    or board[i][j] == board[i][j + 1])):
                    return True
        return False
    
    def is_left_possible(self, board):
        '''
        Returns true if left move is possible, False otherwise.

        Perameters:
            board (list of list): 2048 board the function checks for.

        Returns:
            (boolean): True if move is legal, false otherwise
        '''
        for i in range(4):
            for j in range(1, 4):
                if (board[i][j] != None and (board[i][j - 1] == None
                    or board[i][j] == board[i][j - 1])):
                    return True
        return False
    
    def is_down_possible(self, board):
        '''
        Returns true if down move is possible, False otherwise.

        Perameters:
            board (list of list): 2048 board the function checks for.

        Returns:
            (boolean): True if move is legal, false otherwise
        '''
        for i in range(3):
            for j in range(4):
                if (board[i][j] != None and (board[i + 1][j] == None
                    or board[i][j] == board[i + 1][j])):
                    return True
        return False
    
    def is_up_possible(self, board):
        '''
        Returns true if up move is possible, False otherwise.

        Perameters:
            board (list of list): 2048 board the function checks for.

        Returns:
            (boolean): True if move is legal, false otherwise
        '''
        for i in range(1, 4):
            for j in range(4):
                if (board[i][j] != None and (board[i - 1][j] == None
                    or board[i][j] == board[i - 1][j])):
                    return True
        return False

    def show_board(self, board):
        '''
        Prints board to standard output in human readable form.

        Perameters:
            board (list of list): the 2048 board the function prints.
        '''
        print(" ---------------------------------------")
        print("|\t\t\t\t\t|")
        for col in board:
            print("|\t", end="")
            for num in col:
                if num == None:
                    print("-\t", end="")
                else:
                    print(str(num) + "\t", end="")
            print("|")
            print("|\t\t\t\t\t|")
        print(" ---------------------------------------")

    def suggest_move(self):
        '''
        Suggests a move for the current state of the board (the one associated
        with the class). Function assumes user has attempted to stack largest
        tiles towards the bottom of the board.

        Returns:
            (Direction): The direction the function recomends the user moves.
        '''

        # To get the game started, function randomly suggests either left or
        # Down if the moves are availible.
        if self.score < 300:
            if random.randint(0, 1) == 1:
                if self.is_left_possible(self.board):
                    return Direction.LEFT
                elif self.is_down_possible(self.board):
                    return Direction.DOWN
                else:
                    return Direction.RIGHT
            else:
                if self.is_down_possible(self.board):
                    return Direction.DOWN
                elif self.is_left_possible(self.board):
                    return Direction.LEFT
                else:
                    return Direction.RIGHT
        
        # If the last move was up, suggests the user moves down to preserve
        # a preferable game state.
        if (self.last_move_up):
            self.last_move_up = False
            if self.is_down_possible(self.board):
                return Direction.DOWN
        
        # If row is ordered and it is not stable according to the
        # "is_row_stable" function, suggest_move returns Direction.LEFT
        if (self.is_row_ordered(3, self.board) and not self.is_row_stable(3, self.board)):
            return Direction.LEFT

        # creates a set of potential moves
        potential_moves = set()
        lst = list(itertools.combinations_with_replacement('DLR', 3))
        for combination in lst:
            permutations = list(itertools.permutations(combination))
            for perm in permutations:
                potential_moves.add(perm)

        best_moves = None
        best_assesment = -100000

        # Assesses all the potential moves and saves the one with the best
        # assessment.
        for moves in potential_moves:
            new_board = self.copy_board()
            assesment = self.assess_moves(moves, new_board)
            if assesment != None and assesment > best_assesment:
                best_moves = moves
                best_assesment = assesment

        # if best_moves is None, then the only legal direction a player can move
        # must be up, assuming that the game isn't already over.
        if best_moves == None:
            self.last_move_up = True
            return Direction.UP

        # Returns the first move in the best sequence of moves
        if best_moves[0] == 'D':
            return Direction.DOWN
        elif best_moves[0] == 'L':
            return Direction.LEFT
        else:
            return Direction.RIGHT

    def assess_moves(self, moves, board):
        '''
        Given a sequence of 3 moves, the function returns a score assessing
        how good of a game state the moves are likely to leave for board passed
        into the function.

        Perameters:
            board (list of list): 2048 board the function checks for.
            moves (tuple (Direction, Direction, Direction)): Sequence of moves

        Returns:
            score (int): Evaluation of a sequence of moves. Higher score means
                better likely game state.
        '''
        score = 0
        was_bottom_ordered = self.is_row_ordered(3, board)

        # 3 conditionals shown below give extra wieght to the first move
        if (moves[0] == 'L'):
            if not self.is_left_possible(board):
                return None
            
            # Function gives extra weight to a sequence of moves if the first
            # move is left and other moves would distrupt the board unfavorably 
            if (self.is_row_ordered(3, board) and self.could_down_distrupt_bottom(board)):
                score += 1000
        if (moves[0] == 'D'):
            if not self.is_down_possible(board):
                return None
            
            # If the first move is down, and this would likely distrupt the
            # board, points are taken away
            if (self.is_row_ordered(3, board) and self.could_down_distrupt_bottom(board)):
                score -= 200
        if (moves[0] == 'R'):
            if not self.is_right_possible(board):
                return None
            if (self.is_row_ordered(3, board) and self.could_down_distrupt_bottom(board)):
                score -= 200

            # If the bottom row is stable and ordered, function gives weight to
            # Right move
            if (self.is_row_ordered(3, board) and self.is_row_stable(3, board)):
                score += 8

        # temp variables before moves are made
        temp_score = self.score
        old_bottom_row_score = self.bottom_row_score(board)

        # Goes through moves, game score is automatically updated by the class
        for move in moves:
            if move == 'D':
                if self.is_down_possible(board):
                    self.move(Direction.DOWN, board)
            elif move == 'L':
                if self.is_left_possible(board):
                    
                    # Statement below gives wieght to sequences that don't mess
                    # up the bottom of the board
                    if (self.is_row_ordered(3, board) and self.could_down_distrupt_bottom(board)):
                        score += 100
                    self.move(Direction.LEFT, board)
            elif move == 'R':
                score -= 4
                if self.is_right_possible(board):

                    # Statement below gives wieght to sequences that don't mess
                    # up the bottom of the board
                    if (self.is_row_ordered(3, board) and not self.is_row_stable(3, board)):
                        score -= 5000
                    self.move(Direction.RIGHT, board)
            else:
                logging.error('NOT A VALID DIRECTION.')
        score_improvement = self.score - temp_score
        new_bottom_row_score = self.bottom_row_score(board)

        # Conditionals below gives wieght to sequences that don't mess
        # up the bottom of the board
        if self.is_row_ordered(3, board):
            score += 1000
        if self.loc_largest_piece(board) == (3, 0):
            score += 10000
        
        self.score = temp_score
        return score_improvement + score + 4 * (new_bottom_row_score - old_bottom_row_score)

    def copy_board(self):
        '''
        Returns a copy of the board associated with the 2048game class.

        Returns:
            rv (list of list): a copy of the board stored in self.board
        '''
        rv = []
        for row in self.board:
            row_copy = row.copy()
            rv.append(row_copy)
        return rv

    def is_row_stable(self, row, board):
        '''
        Returns True if the row won't move if the user moves to the right or
        the left.

        Returns:
            (boolean): True if the row is stable, False otherwise
        '''
        if (board[row][0] == None or board[row][1] == None or 
            board[row][2] == None or board[row][3] == None):
            return False
        if (board[row][0] == board[row][1] or 
            board[row][1] == board[row][2] or
            board[row][2] == board[row][3]):
            return False
        return True
    
    def could_down_distrupt_bottom(self, board):
        '''
        Returns true if the next move being down could distrupt bottom row
        of the board passed to the function.

        Perameters:
            board (list of list): 2048 board function preforms check on
        
        Returns:
            (boolean): True if down move could distrupt the bottom row
        '''
        for i in range(1, 4):
            if board[3][i] != None and board[3][i - 1] == None:
                return True
        return False
    
    def is_row_ordered(self, row, board):
        '''
        Return true if row is ordered left to right. Function ignores and
        tiles in the row that are None.

        Perameters:
            row (int): The index of the row in the board to be checked.
            board (list of list): the 2048 board the function checks.
        
        Returns:
            (boolean): True if the row is ordered left to right, False otherwise
        '''
        last_piece = None
        for i in range(4):
            if (last_piece != None and board[row][i] != None and 
                board[row][i] > last_piece):
                return False
            if (board[row][i] != None):
                last_piece = board[row][i]
        return True

    def bottom_row_score(self, board):
        '''
        Returns the sum of all the tiles in the bottom row of the board passed
        to the function. Function ignores any tiles that are None in the
        bottom row.

        Perameters:
            board (list of list): The 2048 board the score is calculated on
        
        Returns:
            score (int): The sum of all the tiles in the bottom row.
        '''
        score = 0
        for num in board[3]:
            if num != None:
                score += num
        return score
