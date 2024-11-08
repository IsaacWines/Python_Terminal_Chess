class Chess:
    def __init__(self,players):

        # if players == 1, set bot
        if players == 1:
            self.players = "bots"
        elif players == 2:
            self.players = "nobots"

        self.piece_dict = {
            # white pieces
            "wP1": ["wP","w","a2"],
            "wP2": ["wP","w","b2"],
            "wP3": ["wP","w","c2"],
            "wP4": ["wP","w","d2"],
            "wP5": ["wP","w","e2"],
            "wP6": ["wP","w","f2"],
            "wP7": ["wP","w","g2"],
            "wP8": ["wP","w","h2"],
            "wR1": ["wR","w","a1"],
            "wR2": ["wR","w","h1"],
            "wN1": ["wN","w","b1"],
            "wN2": ["wN","w","g1"],
            "wB1": ["wB","w","c1"],
            "wB2": ["wB","w","f1"],
            "wK":  ["wK","w","d1"],
            "wQ":  ["wQ","w","e1"],

            # black pieces
            "bP1": ["bP","b","a7"],
            "bP2": ["bP","b","b7"],
            "bP3": ["bP","b","c7"],
            "bP4": ["bP","b","d7"],
            "bP5": ["bP","b","e7"],
            "bP6": ["bP","b","f7"],
            "bP7": ["bP","b","g7"],
            "bP8": ["bP","b","h7"],
            "bR1": ["bR","b","a8"],
            "bR2": ["bR","b","h8"],
            "bN1": ["bN","b","b8"],
            "bN2": ["bN","b","g8"],
            "bB1": ["bB","b","c8"],
            "bB2": ["bB","b","f8"],
            "bK":  ["bK","b","d8"],
            "bQ":  ["bQ","b","e8"]
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
            "h": 8
        }
    
    def set_board(self):
        # initial board set, run pre-game
        self.board = {
            # black pieces
            # [self.piece_dict["bR1"],self.piece_dict["bN1"],self.piece_dict["bB1"],self.piece_dict["bK"],self.piece_dict["bQ"],self.piece_dict["bB2"],self.piece_dict["bN2"],self.piece_dict["bR2"]],
            8: [self.piece_dict["bR1"],self.piece_dict["bN1"],self.piece_dict["bB1"],self.piece_dict["bK"],self.piece_dict["bQ"],self.piece_dict["bB2"],self.piece_dict["bN2"],self.piece_dict["bR2"]],
            7: [self.piece_dict["bP1"],self.piece_dict["bP2"],self.piece_dict["bP3"],self.piece_dict["bP4"],self.piece_dict["bP5"],self.piece_dict["bP6"],self.piece_dict["bP7"],self.piece_dict["bP8"]],
            # blank spaces 
            6: [[" "," ","a6"],[" "," ","b6"],[" "," ","c6"],[" "," ","d6"],[" "," ","e6"],[" "," ","f6"],[" "," ","g6"],[" "," ","h6"]],
            5: [[" "," ","a5"],[" "," ","b5"],[" "," ","c5"],[" "," ","d5"],[" "," ","e5"],[" "," ","f5"],[" "," ","g5"],[" "," ","h5"]],
            4: [[" "," ","a4"],[" "," ","b4"],[" "," ","c4"],[" "," ","d4"],[" "," ","e4"],[" "," ","f4"],[" "," ","g4"],[" "," ","h4"]],
            3: [[" "," ","a3"],[" "," ","b3"],[" "," ","c3"],[" "," ","d3"],[" "," ","e3"],[" "," ","f3"],[" "," ","g3"],[" "," ","h3"]],
            # white pieces
            2: [self.piece_dict["wP1"],self.piece_dict["wP2"],self.piece_dict["wP3"],self.piece_dict["wP4"],self.piece_dict["wP5"],self.piece_dict["wP6"],self.piece_dict["wP7"],self.piece_dict["wP8"]],
            1: [self.piece_dict["wR1"],self.piece_dict["wN1"],self.piece_dict["wB1"],self.piece_dict["wK"],self.piece_dict["wQ"],self.piece_dict["wB2"],self.piece_dict["wN2"],self.piece_dict["wR2"]]
        }
    
    def input_validator(self,selected_space,target_space):
        # if statement to make sure selected and target spaces are valid
        # try:
        selected_space = [selected_space[0],int(selected_space[1])]
        scolumn = self.quick_board[selected_space[0]]
        target_space = [target_space[0],int(target_space[1])]
        tcolumn = self.quick_board[target_space[0]]
        if len(list(selected_space)) == 2 and len(list(target_space)) == 2:
            if (selected_space[0] in list("abcdefgh") and int(selected_space[1]) in [1,2,3,4,5,6,7,8]) and (target_space[0] in list("abcdefgh") and int(target_space[1]) in [1,2,3,4,5,6,7,8]):
                if self.board[selected_space[1]][scolumn] != " " and (self.board[selected_space[1]][scolumn][1] != self.board[target_space[1]][tcolumn]):
                    return True
                else:
                    print(1)
                    return False
            else:
                print(2)
                return False
        else:
            print(3)
            return False
        # except:
        #     print(4)
        #     return False
        
    def user_inputs(self,selected_space,target_space):
        # gets the target space and current piece from user input
        """self.piece = (column,row) | self.target = (column,row)"""
        valid_flag = self.input_validator(selected_space,target_space)
        if valid_flag:
            self.piece = (self.quick_board[selected_space[0]],int(selected_space[1]))
            self.target = (self.quick_board[target_space[0]],int(target_space[1]))
            return True
        else:
            return False
        
    def pred_pawn(self):
        # predictions all possible pawn moves
        """Returns a list of possible moves"""
        pass
    def pred_rook(self):
        # predictions all possible rook moves
        """Returns a list of possible moves"""
        move_list = []

        # checks for piece pos and color
        current_pos = self.board[self.piece[1]][self.piece[0]]
        color = self.board[self.piece[1]][self.piece[0]][1]
        if color == 'b':
            opp_color = 'w'
        elif color == 'w':
            opp_color = 'b'

        # Checks possible moves on the row
        right = []
        left = []

        for index,state in enumerate(self.board[self.piece[1]]):
            print(index)
            if index < self.piece[0]:
                left.append(state)
            elif index == self.piece[0]:
                continue
            else:
                right.append(state)
        print(left, "\n", right)
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

        for row_state in right:
            if row_state[1] == opp_color:
                    move_list.append(row_state[2])
                    break
            elif row_state[1] == color:
                break
            else:
                move_list.append(row_state[2])
        
        # checks moves on the column
        for index in self.board.keys():
            print(index, self.board[index][self.piece[0]][1])
            # if index == self.piece[1]:
            #     continue
            # elif self.board[index][self.piece[0]][1] == opp_color:
            #     move_list.append(self.board[index][self.piece[0]][2])
            #     print(0)
            #     break
            # elif self.board[index][self.piece[0]][1] == color:
            #     print(1)
            #     break
            # else:
            #     move_list.append(self.board[index][self.piece[0]][2])
        return move_list

chess = Chess(2)
chess.set_board()
print(chess.user_inputs("a8","a7"))
print(chess.pred_rook())