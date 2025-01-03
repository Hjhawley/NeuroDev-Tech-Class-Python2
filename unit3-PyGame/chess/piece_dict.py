piece_icons = {
    "black": {
        "queen": "assets/black_queen.png",
        "pawn": "assets/black_pawn.png",
        "rook": "assets/black_rook.png",
        "king": "assets/black_king.png",
        "bishop": "assets/black_bishop.png",
        "knight": "assets/black_knight.png",
    },
    "white": {
        "queen": "assets/white_queen.png",
        "pawn": "assets/white_pawn.png",
        "rook": "assets/white_rook.png",
        "king": "assets/white_king.png",
        "bishop": "assets/white_bishop.png",
        "knight": "assets/white_knight.png",
    }
}

my_pieces = {
    "black": {
            "rook": [(0, 0), (0, 7)],
            "knight": [(0, 1), (0, 6)],
            "bishop": [(0, 2), (0, 5)],
            "queen":  [(0, 3)], 
            "king":  [(0, 4)], 
            "pawn": [(1, x) for x in range(8)]
        },
        
    "white": {
            "rook": [(7, 0), (7, 7)],
            "knight": [(7, 1), (7, 6)],
            "bishop": [(7, 2), (7, 5)],
            "queen":  [(7, 3)], 
            "king":  [(7, 4)],
            "pawn": [(6, x) for x in range(8)]
        }
    }
