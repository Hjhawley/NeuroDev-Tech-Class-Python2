# Chess Game Final Project

import pygame
from pygame.locals import *
from piece_dict import piece_icons, my_pieces

# Chess Piece Classes

class ChessPiece:
    """
    Parent class for every chess piece.
    
    Attributes:
        color (str): 'white' or 'black'
        row (int): the piece's row position on the board (0 to 7)
        col (int): the piece's column position on the board (0 to 7)
        surf (pygame.Surface): the piece's image or sprite
        rect (pygame.Rect): the rectangle bounding the piece (used for drawing)

    Methods to implement or override in child classes:
        get_valid_moves(board):
            Return a list of (row, col) tuples for squares where this piece can legally move.
    """

    def __init__(self, color, row, col, piece_type):
        """
        Initialize the piece with color, row, col, and optionally an image_path.
        """
        self.color = color
        self.row = row
        self.col = col
        self.piece_type = piece_type
        
        # Load the image path from piece_icons
        image_path = piece_icons[color][piece_type]
        
        # Use pygame.image.load to load the PNG
        self.surf = pygame.image.load(image_path).convert_alpha()
        
        # For positioning on the board:
        self.rect = self.surf.get_rect()
        # based on the row,col and your tile size

    def get_valid_moves(self, board):
        """
        Return a list of valid moves (row, col) for this piece given the board state.
        By default, returns an empty list. Override in child classes.
        """
        return []


class King(ChessPiece):
    """
    King piece: moves 1 square in any direction (if not blocked).
    """

    def get_valid_moves(self, board):
        """
        Return a list of valid (row, col) moves for the King.
        """

        return []


class Queen(ChessPiece):
    """
    Queen piece: moves any number of squares along rank, file, or diagonal.
    """

    def get_valid_moves(self, board):
        """
        Return a list of valid (row, col) moves for the Queen.
        """

        return []


class Rook(ChessPiece):
    """
    Rook piece: moves any number of squares along a rank or file.
    """

    def get_valid_moves(self, board):
        """
        Return a list of valid (row, col) moves for the Rook.
        """

        return []


class Bishop(ChessPiece):
    """
    Bishop piece: moves any number of squares diagonally.
    """

    def get_valid_moves(self, board):
        """
        Return a list of valid (row, col) moves for the Bishop.
        """

        return []


class Knight(ChessPiece):
    """
    Knight piece: moves in an 'L' shape (2 squares in one direction + 1 in perpendicular).
    """

    def get_valid_moves(self, board):
        """
        Return a list of valid (row, col) moves for the Knight.
        """

        return []


class Pawn(ChessPiece):
    """
    Pawn piece: moves forward (1 or 2 squares on initial move), captures diagonally.
    Skipping advanced rules like en passant unless students want extra credit.
    """

    def get_valid_moves(self, board):
        """
        Return a list of valid (row, col) moves for the Pawn.
        """

        return []


# Chess Board Class

class ChessBoard:
    """
    Manages an 8x8 grid of ChessPiece objects (or None if empty).
    Also handles drawing the board, selecting pieces, and turn-taking.
    
    Attributes:
        board (list of lists): 8x8 array storing ChessPiece objects or None.
        current_player (str): 'white' or 'black'.
        selected_piece (ChessPiece or None): The piece currently selected by the user.

    Methods:
        setup_board():
            Populate the board with the correct pieces in starting positions.
        draw_board(screen):
            Draw the 8x8 chess grid (tiles), plus all pieces on it.
        handle_click(row, col):
            Handle what happens when the user clicks on row,col.
            - If no piece is selected, select the piece at row,col (if it matches current_player).
            - If a piece is selected, try to move it to row,col (if it's a valid move).
        switch_turn():
            Swap 'white' <-> 'black'.
    """

    def __init__(self):
        """
        Initialize the board data structure.
        Create an 8x8 array of None.
        """
        self.board = [[None for square in range(8)] for square in range(8)]
        self.current_player = 'white'
        self.selected_piece = None
        self.setup_board()

    def setup_board(self):
        """
        Place all pieces (Rook, Knight, Bishop, Queen, King, Pawn) at their starting positions
        using the my_pieces dictionary from piece_dict.
        """

        # Map string piece types to the actual piece classes
        piece_map = {
            "pawn":   Pawn,
            "rook":   Rook,
            "knight": Knight,
            "bishop": Bishop,
            "queen":  Queen,
            "king":   King
        }

        # For each color ('black' or 'white')
        for color, piece_types in my_pieces.items():
            # For each piece type ('pawn', 'rook', etc.) and its list of positions
            for piece_type, positions in piece_types.items():
                # For each (row, col) where that piece should start
                for (row, col) in positions:
                    # Create the piece (constructor requires color, row, col, piece_type)
                    piece_obj = piece_map[piece_type](color, row, col, piece_type)
                    # Place it on the board
                    self.board[row][col] = piece_obj

    def draw_board(self, screen):
        """
        Draw an 8x8 chessboard. Then draw each piece in self.board.
        
        1) Draw squares (two colors).
        2) For each piece in the board, draw piece.surf onto the screen at the right position.
        """

        # They should draw squares in a loop, then piece images if they exist.
        pass

    def handle_click(self, row, col):
        """
        Handle the logic when the user clicks on a given board cell:
        
        1) If self.selected_piece is None:
           - If there's a piece at (row, col), and it matches self.current_player, select it.
        2) Else if self.selected_piece is not None:
           - Check if (row, col) is in the valid moves of the selected piece.
           - If valid, move it. If not, ignore or deselect.
        """

        pass

    def switch_turn(self):
        """
        Switch from 'white' to 'black' or 'black' to 'white'.
        """

        pass

    def move_piece(self, piece, row, col):
        """
        Move the selected piece to (row, col) if it's a valid move.
        1) Remove the piece (if any) at (row, col) (capture).
        2) Update the piece's position.
        3) Place the piece in the board array at (row, col).
        4) Clear the old board position.
        5) Switch turn after successful move.
        """

        pass


# Main game loop

def main():
    """
    Main PyGame loop. Set up the screen, create a ChessBoard, and run an event loop.
    
    Steps:
        1) Initialize PyGame.
        2) Create a screen (e.g., 800x800 for an 8x8 board if each square is 100 px).
        3) Create a ChessBoard.
        4) In a loop:
            - Check pygame.event.get() for QUIT or MOUSEBUTTONDOWN.
            - If user clicks, compute (row, col) from the mouse position (using integer division).
            - Call chessboard.handle_click(row, col).
            - Then chessboard.draw_board(screen) and pygame.display.flip() to update.
        5) On QUIT, break the loop and quit.
    """
    # 1) Initialize PyGame
    pygame.init()
    
    # 2) Create a screen 
    #    Example: 800x800 for 8x8 squares of 100 px each
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Chess Game")
    
    # 3) Create a ChessBoard instance
    chessboard = ChessBoard()
    
    # 4) Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            # On mouse click:
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Convert x,y pixel coords to row,col on the board
                # (Assume each square is screen_width//8 by screen_height//8)
                square_width = screen_width // 8
                square_height = screen_height // 8
                col = mouse_x // square_width
                row = mouse_y // square_height
                
                chessboard.handle_click(row, col)
        
        # Clear the screen (fill with a color, e.g. white)
        screen.fill((255, 255, 255))
        
        # Draw the board
        chessboard.draw_board(screen)
        
        # Flip / update the display
        pygame.display.flip()
    
    # When loop ends, quit PyGame
    pygame.quit()


if __name__ == "__main__":
    main()
