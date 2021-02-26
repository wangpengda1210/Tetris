# Write your code here
import numpy as np


def print_piece(piece_to_print, row, col):
    for pos in range(row * col):
        if pos in piece_to_print or pos in cell_positions:
            print(0, end='')
        else:
            print('-', end='')

        if (pos + 1) % col == 0:
            print()
        else:
            print(' ', end='')

    print()


def should_stop(piece: np.ndarray, rotation: int, row: int, col: int):
    if piece[rotation].max() >= (row - 1) * col:
        return True

    for cell in piece[rotation] + col:
        if cell in cell_positions:
            return True

    return False


def check_game_over(col: int):
    if len(cell_positions) == 0 or min(cell_positions) >= col:
        return False
    else:
        return True


def clear_full_lines(row: int, col: int):
    for i in range(row):
        is_full_line = True
        for j in range(col):
            if not i * col + j in cell_positions:
                is_full_line = False
                break

        if is_full_line:
            for j in range(col):
                cell_positions.remove(i * col + j)
            for index, cell in enumerate(cell_positions):
                if cell < i * col:
                    cell_positions[index] = cell_positions[index] + col


pieces = {'T': np.array([[4, 14, 24, 15], [4, 13, 14, 15],
                         [5, 15, 25, 14], [4, 5, 6, 15]]),
          'O': np.array([[4, 14, 15, 5]]),
          'L': np.array([[4, 14, 24, 25], [5, 15, 14, 13],
                         [4, 5, 15, 25], [6, 5, 4, 14]]),
          'J': np.array([[5, 15, 25, 24], [15, 5, 4, 3],
                         [5, 4, 14, 24], [4, 14, 15, 16]]),
          'I': np.array([[4, 14, 24, 34], [3, 4, 5, 6]]),
          'S': np.array([[5, 4, 14, 13], [4, 14, 15, 25]]),
          'Z': np.array([[4, 5, 15, 16], [5, 15, 14, 24]])}

piece = None
row = None
col = None
rotation = None
cell_positions = []

while True:
    if check_game_over(col):
        print('Game Over!')
        break

    command = input()

    if command == 'exit':
        break

    if command[0].isdigit() and len(command.split()) == 2:
        col, row = command.split()
        col = int(col)
        row = int(row)
        print_piece([], row, col)
        if isinstance(piece, np.ndarray):
            print_piece(piece[rotation], row, col)
    elif command in pieces:
        piece = pieces[command].copy()
        rotation = 0
        if isinstance(row, int) and isinstance(col, int):
            print_piece(piece[rotation], row, col)
    elif command in ['rotate', 'left', 'right', 'down']:
        if not isinstance(piece, np.ndarray) or row is None or col is None:
            print('Please define piece and dimension first')
        else:
            if not should_stop(piece, rotation, row, col):
                piece = piece + col

                if command == 'rotate':
                    rotation += 1
                    if rotation >= len(piece):
                        rotation = 0
                elif command == 'left':
                    if (piece[rotation] % 10).all():
                        piece = piece - 1
                elif command == 'right':
                    if ((piece[rotation] - 9) % 10).all():
                        piece = piece + 1
            else:
                cell_positions = list(set(cell_positions + [cell for cell in piece[rotation]]))

            print_piece(piece[rotation], row, col)
    elif command == 'break':
        if not isinstance(piece, np.ndarray) or row is None or col is None:
            print('Please define piece and dimension first')
        else:
            clear_full_lines(row, col)
            piece = None
            print_piece([], row, col)

