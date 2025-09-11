import chess

# 创建一个新的棋盘（初始局面）
board = chess.Board()
print("初始棋盘:")
print(board)
print("\n合法移动:", list(board.legal_moves)[:10])  # 显示前10个合法移动

# 走棋（使用标准代数记法）
board.push_san("e4")  # 白方王前兵进两格
board.push_san("e5")  # 黑方王前兵进两格
board.push_san("Qh5") # 白后到h5
board.push_san("Nc6") # 黑马到c6
board.push_san("Bc4") # 白象到c4
board.push_san("Nf6") # 黑马到f6
board.push_san("Qxf7#") # 白后吃f7兵，将死！

print("\n最终局面:")
print(board)
print("是否将死?", board.is_checkmate())