class Chess:
    def __init__(self,players):

        # if players == 1, set bot
        if players == 1:
            self.players = "bots"
        elif players == 2:
            self.players = "nobots"

        self.piece_dict = {
            "bP1": ["bP","a7"],
            "bP2": ["bP","b7"],
            "bP3": ["bP","c7"],
            "bP4": ["bP","d7"],
            "bP5": ["bP","e7"],
            "bP6": ["bP","f7"],
            "bP7": ["bP","g7"],
            "bP8": ["bP","h7"],
            "bR1": ["bR","a8"],
            "bR2": ["bR","h8"],
            "bN1": ["bN","b8"],
            "bN2": ["bN","g8"],
            
        }