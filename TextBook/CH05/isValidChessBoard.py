{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
def is_valid_chess_board(board):
    # 駒の名前と駒数のカウントを初期化
    piece_count = {'w': 0, 'b': 0}
    piece_type_count = {'wpawn': 0, 'bpawn': 0, 'wking': 0, 'bking': 0}
    
    # 駒の位置が有効かどうかをチェックする関数
    def is_valid_position(pos):
        if len(pos) != 2:
            return False
        row, col = pos
        return row in '12345678' and col in 'abcdefgh'
    
    # 駒の名前が有効かどうかをチェックする関数
    def is_valid_piece(piece):
        if len(piece) < 2:
            return False
        color, piece_type = piece[0], piece[1:]
        valid_colors = {'w', 'b'}
        valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
        return color in valid_colors and piece_type in valid_pieces
    
    for position, piece in board.items():
        # 駒の位置のチェック
        if not is_valid_position(position):
            return False
        
        # 駒の名前のチェック
        if not is_valid_piece(piece):
            return False
        
        # 駒の数のカウント
        piece_count[piece[0]] += 1
        if piece in piece_type_count:
            piece_type_count[piece] += 1
    
    # 各プレイヤーの駒の数が16以下であるかのチェック
    if piece_count['w'] > 16 or piece_count['b'] > 16:
        return False
    
    # 白と黒のキングがそれぞれ1つ存在するかのチェック
    if piece_type_count['wking'] != 1 or piece_type_count['bking'] != 1:
        return False
    
    # ポーンの数が8以下であるかのチェック
    if piece_type_count['wpawn'] > 8 or piece_type_count['bpawn'] > 8:
        return False
    
    return True

# テストケース
chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(is_valid_chess_board(chess_board))  # 結果: True
