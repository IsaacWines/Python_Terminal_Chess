class Chess:
    def __init__(self,players):

        # if players == 1, set bot
        if players == 1:
            self.players = "bots"
        elif players == 2:
            self.players = "nobots"

        self.piece_dict = {
            # white pieces
            "wP1": ["wP", "w", "a2", 0],
            "wP2": ["wP", "w", "b2", 0],
            "wP3": ["wP", "w", "c2", 0],
            "wP4": ["wP", "w", "d2", 0],
            "wP5": ["wP", "w", "e2", 0],
            "wP6": ["wP", "w", "f2", 0],
            "wP7": ["wP", "w", "g2", 0],
            "wP8": ["wP", "w", "h2", 0],
            "wR1": ["wR", "w", "a1", 0],
            "wR2": ["wR", "w", "h1", 0],
            "wN1": ["wN", "w", "b1", 0],
            "wN2": ["wN", "w", "g1", 0],
            "wB1": ["wB", "w", "c1", 0],
            "wB2": ["wB", "w", "f1", 0],
            "wK": ["wK", "w", "d1", 0],
            "wQ": ["wQ", "w", "e1", 0],

            # black pieces
            "bP1": ["bP", "b", "a7", 0],
            "bP2": ["bP", "b", "b7", 0],
            "bP3": ["bP", "b", "c7", 0],
            "bP4": ["bP", "b", "d7", 0],
            "bP5": ["bP", "b", "e7", 0],
            "bP6": ["bP", "b", "f7", 0],
            "bP7": ["bP", "b", "g7", 0],
            "bP8": ["bP", "b", "h7", 0],
            "bR1": ["bR", "b", "a8", 0],
            "bR2": ["bR", "b", "h8", 0],
            "bN1": ["bN", "b", "b8", 0],
            "bN2": ["bN", "b", "g8", 0],
            "bB1": ["bB", "b", "c8", 0],
            "bB2": ["bB", "b", "f8", 0],
            "bK": ["bK", "b", "d8", 0],
            "bQ": ["bQ", "b", "e8", 0]
        }

        # dict to quickly convert the board letter to a index
        self.quick_board = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7
        }

        self.quick_board_rev = {v: k for k, v in self.quick_board.items()}

        # dict for running the predictions
        self.pred_dict = {
            "bP": lambda: self.pred_pawn(),
            "wP": lambda: self.pred_pawn(),
            "bN": lambda: self.pred_knight(),
            "wN": lambda: self.pred_knight(),
            "bB": lambda: self.pred_bishop(),
            "wB": lambda: self.pred_bishop(),
            "bK": lambda: self.pred_king(),
            "wK": lambda: self.pred_king(),
            "bR": lambda: self.pred_rook(),
            "wR": lambda: self.pred_rook(),
            "wQ": lambda: self.pred_queen(),
            "bQ": lambda: self.pred_queen()
        }

        self.current_turn = "w"  # Track the current player's turn
        self.bot = "b"  # Track the bot's color

    def set_board(self):    
        """Sets the initial state of the board, run before the game starts"""
        self.board = {
            8: [self.piece_dict["bR1"], self.piece_dict["bN1"], self.piece_dict["bB1"], self.piece_dict["bK"], self.piece_dict["bQ"], self.piece_dict["bB2"], self.piece_dict["bN2"], self.piece_dict["bR2"]],
            7: [self.piece_dict["bP1"], self.piece_dict["bP2"], self.piece_dict["bP3"], self.piece_dict["bP4"], self.piece_dict["bP5"], self.piece_dict["bP6"], self.piece_dict["bP7"], self.piece_dict["bP8"]],
            6: [[" ", " ", "a6", 0], [" ", " ", "b6", 0], [" ", " ", "c6", 0], [" ", " ", "d6", 0], [" ", " ", "e6", 0], [" ", " ", "f6", 0], [" ", " ", "g6", 0], [" ", " ", "h6", 0]],
            5: [[" ", " ", "a5", 0], [" ", " ", "b5", 0], [" ", " ", "c5", 0], [" ", " ", "d5", 0], [" ", " ", "e5", 0], [" ", " ", "f5", 0], [" ", " ", "g5", 0], [" ", " ", "h5", 0]],
            4: [[" ", " ", "a4", 0], [" ", " ", "b4", 0], [" ", " ", "c4", 0], [" ", " ", "d4", 0], [" ", " ", "e4", 0], [" ", " ", "f4", 0], [" ", " ", "g4", 0], [" ", " ", "h4", 0]],
            3: [[" ", " ", "a3", 0], [" ", " ", "b3", 0], [" ", " ", "c3", 0], [" ", " ", "d3", 0], [" ", " ", "e3", 0], [" ", " ", "f3", 0], [" ", " ", "g3", 0], [" ", " ", "h3", 0]],
            2: [self.piece_dict["wP1"], self.piece_dict["wP2"], self.piece_dict["wP3"], self.piece_dict["wP4"], self.piece_dict["wP5"], self.piece_dict["wP6"], self.piece_dict["wP7"], self.piece_dict["wP8"]],
            1: [self.piece_dict["wR1"], self.piece_dict["wN1"], self.piece_dict["wB1"], self.piece_dict["wK"], self.piece_dict["wQ"], self.piece_dict["wB2"], self.piece_dict["wN2"], self.piece_dict["wR2"]]
        }

    def print_board(self):
        """Prints the current state of the board"""
        print("    a    b    c    d    e    f    g    h")
        print("  -----------------------------------------")
        for row in range(8, 0, -1):  # Start from row 8 to 1
            print(f"{row} |", end="")  # Print row number
            for col in range(8):
                piece = self.board[row][col][0]  # Get piece name
                if piece.strip():
                    print(f" {piece} |", end="")
                else:
                    print("    |", end="")
            print(f" {row}", end = "")
            print("\n  -----------------------------------------")

        # Print column letters
        print("    a    b    c    d    e    f    g    h\n")

    def debug_board(self):
        for row in self.board.keys():
            print(self.board[row])
            print("-----------------")

    def move_piece(self):
        """Updates position of pieces on the board"""
        selected_row = int(self.piece[1])
        selected_col = int(self.piece[0])

        target_row = int(self.target[1])
        target_col = int(self.target[0])

        # Get the piece being moved
        piece = self.board[selected_row][selected_col]
    
        # Update the move count
        piece[3] += 1

        # Update the piece's position in piece_dict
        piece[2] = self.board[target_row][target_col][2]

        # Empty the original space
        self.board[selected_row][selected_col] = [" ", " ", f"{self.quick_board_rev[selected_col]}{selected_row}", 0] 
        
        # Move the piece to the target space
        self.board[target_row][target_col] = piece

        # Change the current turn
        if self.current_turn == "w":
            self.current_turn = "b"
        else:
            self.current_turn = "w"

    def possibile_moves(self):
        """Gets all possible moves for a selected piece"""
        selected_row = int(self.piece[1])
        selected_col = int(self.piece[0])
        try:
            return self.pred_dict[self.board[selected_row][selected_col][0]]()
        except:
            return "No possible moves"

    def move_logic(self):
        """Takes in the selected and target piece and moves said piece based on the prediction functions"""
        selected_row = int(self.piece[1])
        selected_col = int(self.piece[0])
        target_row = int(self.target[1])
        target_col = int(self.target[0])
        
        try:
            self.poss_moves = self.pred_dict[self.board[selected_row][selected_col][0]]()
        except:
            return False
        if self.board[target_row][target_col][2] in self.poss_moves:
            self.move_piece()    
            return True   
        else:
            return False

    def input_validator(self,selected_space,target_space):
        """Validates the user input, makes sure the input is able to be used by the program"""
        try:
            selected_space = [selected_space[0],int(selected_space[1])]
            scolumn = self.quick_board[selected_space[0]]
            target_space = [target_space[0],int(target_space[1])]
            tcolumn = self.quick_board[target_space[0]]
        except:
            return False
        if target_space[0] not in "abcdefgh" or selected_space[0] not in "abcdefgh" or \
           target_space[1] not in range(1, 9) or selected_space[1] not in range(1, 9):
            return False
        else:
            return True
        
    def user_inputs(self,selected_space,target_space):
        """gets the target space and current piece from user input\n
        self.piece = (column,row)\n
        self.target = (column,row)"""
        valid_flag = self.input_validator(selected_space,target_space)
        if valid_flag:
            self.piece = (self.quick_board[selected_space[0]],int(selected_space[1]))
            self.target = (self.quick_board[target_space[0]],int(target_space[1]))
            return True
        else:
            return False
        
    def game_condiition(self):
        """
        Check and create the win condiition flag.

            Args:
                self
            Returns:
                True - if win condition is False\n
                False - if win condition is True
        """
        # checks for checkmate, or draw 
        return True
        
    def pred_pawn(self):
        # predictions all possible pawn moves
        """Returns a list of possible moves"""
        move_list = []
        current_row = self.piece[1]
        current_col = self.piece[0]
        color = self.board[current_row][current_col][1]

        if color == 'b':
            opp_color = 'w'
        elif color == 'w':
            opp_color = 'b'

        # check for the two move rule
        if color == 'w':
            if self.board[current_row][current_col][3] == 0:
                potential_moves = [
                    (current_row + 1, current_col + 1, 1),
                    (current_row + 1, current_col - 1, 1),
                    (current_row + 1, current_col, 2),
                    (current_row + 2, current_col, 0)               
                ]

                for move in potential_moves:
                    new_row, new_col, sig = move
                    if not(new_row > 8 or new_row < 1) and not(new_col > 7 or new_col < 0):
                        
                        if sig == 1:
                            if self.board[new_row][new_col][1] == opp_color:
                                move_list.append(self.board[new_row][new_col][2])
                        elif sig == 2:
                            if self.board[new_row][new_col][1] == " ":
                                move_list.append(self.board[new_row][new_col][2])
                            else:
                                break
                        else:
                            if self.board[new_row][new_col][1] == " ":
                                move_list.append(self.board[new_row][new_col][2])
            else:
                potential_moves = [
                    (current_row + 1, current_col, 0),
                    (current_row + 1, current_col + 1, 1),
                    (current_row + 1, current_col - 1, 1)
                ]

                for move in potential_moves:
                    new_row, new_col, sig = move
                    if not(new_row > 8 or new_row < 1) and not(new_col > 7 or new_col < 0):
                        
                        if sig == 1:
                            if self.board[new_row][new_col][1] == opp_color:
                                move_list.append(self.board[new_row][new_col][2])
                        else:
                            if self.board[new_row][new_col][1] == " ":
                                move_list.append(self.board[new_row][new_col][2])
        elif color == 'b':
            if self.board[current_row][current_col][3] == 0:
                potential_moves = [
                    (current_row - 1, current_col + 1, 1),
                    (current_row - 1, current_col - 1, 1),
                    (current_row - 1, current_col, 2),
                    (current_row - 2, current_col, 0)               
                ]

                for move in potential_moves:
                    new_row, new_col, sig = move
                    if not(new_row > 8 or new_row < 1) and not(new_col > 7 or new_col < 0):
                        
                        if sig == 1:
                            if self.board[new_row][new_col][1] == opp_color:
                                move_list.append(self.board[new_row][new_col][2])
                        elif sig == 2:
                            if self.board[new_row][new_col][1] == " ":
                                move_list.append(self.board[new_row][new_col][2])
                            else:
                                break
                        else:
                            if self.board[new_row][new_col][1] == " ":
                                move_list.append(self.board[new_row][new_col][2])
            else:
                potential_moves = [
                    (current_row - 1, current_col, 0),
                    (current_row - 1, current_col + 1, 1),
                    (current_row - 1, current_col - 1, 1)
                ]

                for move in potential_moves:
                    new_row, new_col, sig = move
                    if not(new_row > 8 or new_row < 1) and not(new_col > 7 or new_col < 0):
                        
                        if sig == 1:
                            if self.board[new_row][new_col][1] == opp_color:
                                move_list.append(self.board[new_row][new_col][2])
                        else:
                            if self.board[new_row][new_col][1] == " ":
                                move_list.append(self.board[new_row][new_col][2])
        return move_list
    
    def pred_knight(self):
        # predictions all possible knight moves
        """Returns a list of possible moves"""

        current_row = self.piece[1]
        current_col = self.piece[0]
        color = self.board[self.piece[1]][self.piece[0]][1]
        # Calculate potential new positions based on the knight's movement
        potential_moves = [
            (current_row + 2, current_col + 1),
            (current_row + 2, current_col - 1),
            (current_row - 2, current_col + 1),
            (current_row - 2, current_col - 1),
            (current_row + 1, current_col + 2),
            (current_row + 1, current_col - 2),
            (current_row - 1, current_col + 2),
            (current_row - 1, current_col - 2)
        ]

        # Validate the new positions to ensure they are within bounds
        valid_moves = []
        for move in potential_moves:
            new_row, new_col = move
            if not(new_row > 8 or new_row < 1) and not(new_col > 7 or new_col < 0):
                if self.board[new_row][new_col][1] != color:
                    valid_moves.append(self.board[new_row][new_col][2])
        return valid_moves

    def pred_rook(self):
        # predictions all possible rook moves
        """Returns a list of possible moves"""
        move_list = []
    
        # checks for piece pos and color
        color = self.board[self.piece[1]][self.piece[0]][1]
        if color == 'b':
            opp_color = 'w'
        elif color == 'w':
            opp_color = 'b'

        # Checks possible moves on the row
        right = []
        left = []          
        # splits the row into left of piece and right of piece
        for index,state in enumerate(self.board[self.piece[1]]):
            if index < self.piece[0]:
                left.append(state)
            elif index == self.piece[0]:
                continue
            else:
                right.append(state)

        # finds all the possible left moves
        if len(left) > 0:
            left.reverse()
            for row_state in left:
                if row_state[1] == opp_color:
                        move_list.append(row_state[2])
                        break
                elif row_state[1] == color:
                    break
                else:
                    move_list.append(row_state[2])

        # finds all the possible right moves
        for row_state in right:
            if row_state[1] == opp_color:
                    move_list.append(row_state[2])
                    break
            elif row_state[1] == color:
                break
            else:
                move_list.append(row_state[2])
        
        # checks moves on the column
        """Logic for getting the index of pieces above and below selected piece"""
        temp_col = [x for x in range(1,len(self.board.keys())+1)]
        temp_col = "".join(map(str,temp_col))
        temp_col = temp_col.split(str(self.piece[1]))
        up,down = list(temp_col[0]),list(temp_col[1])
        up.reverse()
        """"""

        # checks for movement down the board
        if down != None:
            for index in down:
                index = int(index)
                if self.board[index][self.piece[0]][1] == color:
                    break
                elif self.board[index][self.piece[0]][1] == opp_color:
                    move_list.append(self.board[index][self.piece[0]][2])
                    break
                else:
                    move_list.append(self.board[index][self.piece[0]][2])

        # checks for movement up the board
        if up != None:
            for index in up:
                index = int(index)
                if self.board[index][self.piece[0]][1] == color:
                    break
                elif self.board[index][self.piece[0]][1] == opp_color:
                    move_list.append(self.board[index][self.piece[0]][2])
                    break
                else:
                    move_list.append(self.board[index][self.piece[0]][2])
    
        return move_list

    def pred_bishop(self):
        # predictions all possible bishop moves
        """Returns a list of possible moves"""
        directions = [
            (1, 1),  # Down-right
            (1, -1), # Down-left
            (-1, 1), # Up-right
            (-1, -1) # Up-left
        ]

        # sets rows and colors
        current_row = self.piece[1]
        current_col = self.piece[0]
        color = self.board[self.piece[1]][self.piece[0]][1]
        if color == 'b':
            opp_color = 'w'
        elif color == 'w':
            opp_color = 'b'
        move_list = []
        
        for direction in directions:
            for i in range(1, 8):  # Bishops can move up to 7 squares in any direction
                new_row = current_row + i * direction[0]
                new_col = current_col + i * direction[1]

                # color logic
                if not(new_row > 8 or new_row < 1) and not(new_col > 7 or new_col < 0):

                    if self.board[new_row][new_col][1] == color:
                        break
                    elif self.board[new_row][new_col][1] == opp_color:
                        move_list.append(self.board[new_row][new_col][2])
                        break
                    else:
                        move_list.append(self.board[new_row][new_col][2])
                    
        return move_list

    def pred_king(self):
        # predictions all possible king moves
        """Returns a list of possible moves"""

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
            (1,1),
            (-1,1),
            (1,-1),
            (-1,-1)
        ]

        # sets rows and colors
        current_row = self.piece[1]
        current_col = self.piece[0]
        color = self.board[self.piece[1]][self.piece[0]][1]
        if color == 'b':
            opp_color = 'w'
        elif color == 'w':
            opp_color = 'b'
        move_list = []

        for direction in directions:
            for i in range(1,2):  # Kings can move up to 1 squares in any direction
                new_row = current_row + i * direction[0]
                new_col = current_col + i * direction[1]

                # color logic
                if not(new_row > 8 or new_row < 1) and not(new_col > 7 or new_col < 0):
                    if self.board[new_row][new_col][1] == color:
                        break
                    elif self.board[new_row][new_col][1] == opp_color:
                        move_list.append(self.board[new_row][new_col][2])
                        break
                    else:
                        move_list.append(self.board[new_row][new_col][2])
                    
        return move_list
    
    def pred_queen(self):
        """Returns a list of possible moves for the queen, including all directions."""
        move_list = []
        current_row = self.piece[1]
        current_col = self.piece[0]
        color = self.board[current_row][current_col][1]

        if color == 'b':
            opp_color = 'w'
        elif color == 'w':
            opp_color = 'b'
        
        up = [(current_row + x, current_col) for x in range(1, 8)]
        down = [(current_row - x, current_col) for x in range(1, 8)]
        left = [(current_row, current_col - x) for x in range(1, 8)]
        right = [(current_row, current_col + x) for x in range(1, 8)]
        dia_up_right = [(current_row + x, current_col + x) for x in range(1, 8)]
        dia_up_left = [(current_row + x, current_col - x) for x in range(1, 8)]
        dia_down_right = [(current_row - x, current_col + x) for x in range(1, 8)]
        dia_down_left = [(current_row - x, current_col - x) for x in range(1, 8)]
        
        # Include left and right
        all_moves = [up, down, left, right, dia_up_right, dia_up_left, dia_down_right, dia_down_left]

        for direction in all_moves:
            for move in direction:
                new_row, new_col = move
                # Check if the move is within bounds
                if not (new_row > 8 or new_row < 1) and not (new_col > 7 or new_col < 0):
                    if self.board[new_row][new_col][1] == color:  # Same color piece
                        break
                    elif self.board[new_row][new_col][1] == opp_color:  # Opponent's piece
                        move_list.append(self.board[new_row][new_col][2])
                        break
                    else:  # Empty square
                        move_list.append(self.board[new_row][new_col][2])

        return move_list


def test():
    players = input("Enter number of players: ")
    chess = Chess(players)
    chess.set_board()
    flag = True

    while flag:
        chess.print_board()
        command = input("Enter a command: ")
        if command == "move":
            print("Current Turn: ",chess.current_turn)
            current = input("Select a piece: ")
            target = input("Select a target: ")
            input_flag = chess.user_inputs(current,target)
            
            if input_flag:
                if chess.current_turn != chess.board[chess.piece[1]][chess.piece[0]][1]:
                    print("Invalid Turn")
                    input()
                elif not chess.move_logic():
                    print("Invalid Move")
                    input()
            else:
                print("Invalid Input")
                input()

        if command == "exit":
            flag = False

        if command == "poss":
            current = input("Select a piece: ")
            target = "a1"
            if chess.user_inputs(current,target):
                print(f"Possible moves for {current}: {chess.possibile_moves()}")
                input()
            else:
                print("Input Error")
        
        if command == "debug":
            chess.debug_board()
            input()
            # print("pawn",chess.pred_pawn())
            # print("rook",chess.pred_rook())
            # print("knight",chess.pred_knight())
            # print("bishop",chess.pred_bishop())
            # print("king",chess.pred_king())
            # print("queen",chess.pred_queen())
            input()

if __name__ == "__main__":
    test()
        
