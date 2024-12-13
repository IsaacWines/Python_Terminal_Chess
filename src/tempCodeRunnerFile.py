self.pred_dict = {
            "bP": self.pred_pawn(),
            "wP": self.pred_pawn(),
            "bK": self.pred_knight(),
            "wK": self.pred_knight(),
            "bB": self.pred_bishop(),
            "wB": self.pred_bishop(),
            "bK": self.pred_king,
            "wK": self.pred_king,
            "bR": self.pred_rook(),
            "bR": self.pred_rook()
            # add queen and pawn
        }