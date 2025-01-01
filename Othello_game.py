MOVE_DIRS = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),           (0, 1),
             (1, -1), (1, 0), (1, 1)]


class Othello:
    def __init__(self, board):
        self.board = board
        self.current_player = 'B'

    def print_board(self):
        print("  A B C D E F G H")
        for idx, row in enumerate(self.board):
            print(f"{idx+1} {' '.join(row)}")
        print()

    def is_valid_coord(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def has_tile_to_flip(self, move, direction):
        row, col = move
        dr, dc = direction
        tiles_to_flip = []
        opponent = 'W' if self.current_player == 'B' else 'B'

        while True:
            row += dr
            col += dc
            if not self.is_valid_coord(row, col) or self.board[row][col] == '-':
                return []
            if self.board[row][col] == self.current_player:
                return tiles_to_flip
            if self.board[row][col] == opponent:
                tiles_to_flip.append((row, col))

    def is_legal_move(self, move):
        row, col = move
        if not self.is_valid_coord(row, col) or self.board[row][col] != '-':
            return False
        for direction in MOVE_DIRS:
            if self.has_tile_to_flip(move, direction):
                return True
        return False

    def get_legal_moves(self):
        moves = []
        for row in range(8):
            for col in range(8):
                if self.is_legal_move((row, col)):
                    moves.append((row, col))
        return moves

    def mark_legal_moves(self, moves):
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == '*':
                    self.board[row][col] = '-'
        for row, col in moves:
            self.board[row][col] = '*'
            
    def make_move(self, move):
        row, col = move
        if not self.is_legal_move(move):
            return False

        self.board[row][col] = self.current_player
        for direction in MOVE_DIRS:
            tiles_to_flip = self.has_tile_to_flip(move, direction)
            for r, c in tiles_to_flip:
                self.board[r][c] = self.current_player
        self.current_player = 'W' if self.current_player == 'B' else 'B'
        return True

    def game_over(self):
        return not self.get_legal_moves() and not self.get_legal_moves()

    def play(self):
        while not self.game_over():
            legal_moves = self.get_legal_moves()
            self.print_board()
            if not legal_moves:
                print(f"No valid moves for {self.current_player}. Skipping turn.")
                self.current_player = 'W' if self.current_player == 'B' else 'B'
                continue

            print(f"Available moves: {[chr(c+65) + str(r+1) for r, c in legal_moves]}")
            while True:
                move = input(f"Player {self.current_player}, enter your move (e.g., D8): ").upper().strip()
                if len(move) != 2 or not move[0].isalpha() or not move[1].isdigit():
                    print("Invalid input. Use format like D8.")
                    continue
                col = ord(move[0]) - ord('A')
                row = int(move[1]) - 1
                if self.make_move((row, col)):
                    break
                print("Invalid move. Try again.")

        self.print_board()
        black_count = sum(row.count('B') for row in self.board)
        white_count = sum(row.count('W') for row in self.board)
        print(f"Game Over! Black: {black_count}, White: {white_count}")
        if black_count > white_count:
            print("Black wins!")
        elif white_count > black_count:
            print("White wins!")
        else:
            print("It's a tie!")


def main():
    boards = [
        [
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', 'W', 'B', '-', '-', '-', '-'],
            ['-', '-', 'B', 'W', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-']
        ],
        [
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', 'W', 'B', '-', '-'],
            ['-', '-', '-', '-', 'B', 'W', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-']
        ],
        [
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', 'W', 'B', '-', '-', '-', '-'],
            ['-', '-', 'B', 'W', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-']
        ],
        [
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', 'W', 'B', '-', '-'],
            ['-', '-', '-', '-', 'B', 'W', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-']
        ]
        # Add additional boards as needed
    ]

    print("Choose a starting board (1-4):")
    for i, board in enumerate(boards):
        print(f"Board {i + 1}:")
        for row in board:
            print(' '.join(row))
        print()

    choice = int(input("Enter the board number (1-4): ")) - 1
    if choice < 0 or choice >= len(boards):
        print("Invalid choice. Exiting.")
        return

    game = Othello(boards[choice])
    game.play()


if __name__ == "__main__":
    main()
