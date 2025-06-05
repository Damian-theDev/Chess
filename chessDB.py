import mysql.connector
from mysql.connector import Error
import json
from datetime import datetime

class ChessDatabase:
    def __init__(self):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='chess_user',
                password='chess_password',
                database='chess_ai',
                autocommit=True
            )
        except Exception as e:
            print(f"Database connection error: {e}")

    def start_new_game(self):
        """Create a new game record in the database"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO games (start_datetime) 
                VALUES (NOW())
            """)
            game_id = cursor.lastrowid
            cursor.close()
            return game_id
        except Exception as e:
            print(f"Error starting new game: {e}")
            return None

    def end_game(self, game_id, result):
        """Mark a game as completed with result"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE games 
                SET end_datetime = NOW(),
                    duration_seconds = TIMESTAMPDIFF(SECOND, start_datetime, NOW()),
                    result = %s
                WHERE game_id = %s
            """, (result, game_id))
            cursor.close()
        except Exception as e:
            print(f"Error ending game: {e}")

    def _generate_fen(self, board_matrix):
        """Convert your board matrix to FEN notation"""
        fen_rows = []
        for row in board_matrix:
            fen_row = ''
            empty = 0
            for piece in row:
                if piece is None:
                    empty += 1
                else:
                    if empty > 0:
                        fen_row += str(empty)
                        empty = 0
                    fen_row += piece.type[0].upper() if piece.color == 'white' else piece.type[0].lower()
            if empty > 0:
                fen_row += str(empty)
            fen_rows.append(fen_row)
        return '/'.join(fen_rows) + ' w KQkq - 0 1'

    def _generate_algebraic_notation(self, piece, from_pos, to_pos, is_capture=False):
        """Generate standard algebraic notation"""
        cols = 'abcdefgh'
        from_col, from_row = from_pos[1], 7 - from_pos[0]
        to_col, to_row = to_pos[1], 7 - to_pos[0]
        
        # Castling
        if piece.type == 'king' and abs(to_pos[1] - from_pos[1]) == 2:
            return "O-O" if to_pos[1] > from_pos[1] else "O-O-O"
        
        # Normal moves
        notation = ''
        if piece.type != 'pawn':
            notation += piece.type[0].upper()
        
        notation += cols[from_col] + str(from_row + 1)
        if is_capture:
            notation += 'x'
        notation += cols[to_col] + str(to_row + 1)
        return notation

    def record_move(self, game_id, ply, piece, from_pos, to_pos, board_state, target_piece=None):
        """Record a move with all metadata"""
        try:
            move_data = {
                'game_id': game_id,
                'ply_number': ply,
                'move_notation': self._generate_algebraic_notation(
                    piece, from_pos, to_pos, target_piece is not None
                ),
                'from_row': from_pos[0],
                'from_col': from_pos[1],
                'to_row': to_pos[0],
                'to_col': to_pos[1],
                'piece_type': piece.type[0].upper(),
                'color': piece.color,
                'captured_piece': target_piece.type[0].upper() if target_piece else None,
                'is_castle': piece.type == 'king' and abs(to_pos[1] - from_pos[1]) == 2,
                'fen_before': self._generate_fen(board_state),
            }
            
            # Get FEN after move
            temp_board = [row[:] for row in board_state]
            temp_board[to_pos[0]][to_pos[1]] = temp_board[from_pos[0]][from_pos[1]]
            temp_board[from_pos[0]][from_pos[1]] = None
            move_data['fen_after'] = self._generate_fen(temp_board)

            query = """
            INSERT INTO moves (
                game_id, ply_number, move_notation,
                from_row, from_col, to_row, to_col,
                piece_type, color, captured_piece,
                is_castle, fen_before, fen_after
            ) VALUES (
                %(game_id)s, %(ply_number)s, %(move_notation)s,
                %(from_row)s, %(from_col)s, %(to_row)s, %(to_col)s,
                %(piece_type)s, %(color)s, %(captured_piece)s,
                %(is_castle)s, %(fen_before)s, %(fen_after)s
            )
            """
            
            cursor = self.connection.cursor()
            cursor.execute(query, move_data)
            cursor.close()
            return True
        except Exception as e:
            print(f"Error recording move: {e}")
            return False

    def close(self):
        """Close the database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()