chess_board = {
    'a1': ' ', 'a2': ' ', 'a3': ' ', 'a4': ' ', 'a5': ' ', 'a6': ' ', 'a7': ' ', 'a8': ' ',
    'b1': ' ', 'b2': ' ', 'b3': ' ', 'b4': ' ', 'b5': ' ', 'b6': ' ', 'b7': ' ', 'b8': ' ',
    'c1': ' ', 'c2': ' ', 'c3': ' ', 'c4': ' ', 'c5': ' ', 'c6': ' ', 'c7': ' ', 'c8': ' ',
    'd1': ' ', 'd2': ' ', 'd3': ' ', 'd4': ' ', 'd5': ' ', 'd6': ' ', 'd7': ' ', 'd8': ' ',
    'e1': ' ', 'e2': ' ', 'e3': ' ', 'e4': ' ', 'e5': ' ', 'e6': ' ', 'e7': ' ', 'e8': ' ',
    'f1': ' ', 'f2': ' ', 'f3': ' ', 'f4': ' ', 'f5': ' ', 'f6': ' ', 'f7': ' ', 'f8': ' ',
    'g1': ' ', 'g2': ' ', 'g3': ' ', 'g4': ' ', 'g5': ' ', 'g6': ' ', 'g7': ' ', 'g8': ' ',
    'h1': ' ', 'h2': ' ', 'h3': ' ', 'h4': ' ', 'h5': ' ', 'h6': ' ', 'h7': ' ', 'h8': ' '
}

possible_pieces = ['bking', 'bknight', 'bbishop', 'brook', 'bqueen', 'bpawn',
                   'wking', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wpawn']

test_board = {
    'a1': 'bking', 'a2': 'wpawn', 'a3': 'wpawn', 'a4': ' ', 'a5': ' ', 'a6': ' ', 'a7': ' ', 'a8': ' ',
    'b1': 'wking', 'b2': 'wpawn', 'b3': 'wpawn', 'b4': ' ', 'b5': ' ', 'b6': ' ', 'b7': ' ', 'b8': ' ',
    'c1': 'bpawn', 'c2': 'wpawn', 'c3': 'bbishop', 'c4': ' ', 'c5': ' ', 'c6': ' ', 'c7': ' ', 'c8': ' ',
    'd1': 'bpawn', 'd2': 'wpawn', 'd3': ' ', 'd4': ' ', 'd5': ' ', 'd6': ' ', 'd7': ' ', 'd8': ' ',
    'e1': 'bpawn', 'e2': 'wpawn', 'e3': ' ', 'e4': ' ', 'e5': ' ', 'e6': ' ', 'e7': ' ', 'e8': ' ',
    'f1': 'bpawn', 'f2': 'wpawn', 'f3': ' ', 'f4': ' ', 'f5': ' ', 'f6': ' ', 'f7': ' ', 'f8': ' ',
    'g1': 'bpawn', 'g2': 'bpawn', 'g3': ' ', 'g4': ' ', 'g5': ' ', 'g6': ' ', 'g7': ' ', 'g8': ' ',
    'h1': 'bpawn', 'h2': 'bpawn', 'h3': ' ', 'h4': ' ', 'h5': ' ', 'h6': ' ', 'h7': ' ', 'h8': ' '
}


def isValidChessBoard(board):
    chess_pieces = {}
    is_valid = True

    # Counts the number of pieces of each type on the board
    for x in board.values():
        chess_pieces.setdefault(x, 0)
        chess_pieces[x] = chess_pieces[x] + 1

    # Returns false if there is more than one white king
    try:
        if chess_pieces['wking'] != 1:
            is_valid = False
    except:
        is_valid = False
    try:
        if chess_pieces['wpawn'] > 8:
            is_valid = False
    except:
        pass

    # Returns false if there is more than one black king
    try:
        if chess_pieces['bking'] != 1:
            is_valid = False
    except:
        is_valid = False

    try:
        if chess_pieces['bpawn'] > 8:
            is_valid = False
    except:
        pass

    # Checks to see if the keys are either blank or start with a 'b' or a 'w'
    for c in chess_pieces.keys():
        if c in possible_pieces or c == ' ':
            pass
        else:
            is_valid = False

    # Pulls all possible board positions and checks to see if there are any invalid positions
    board_positions = list(chess_board.keys())
    for b in board_positions:
        if b not in board:
            is_valid = False
    return is_valid


print(isValidChessBoard(test_board))
