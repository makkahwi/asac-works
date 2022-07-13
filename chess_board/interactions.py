from chess_board.chess_board import ChessBoard

# No Attack Case
game1 = ChessBoard()
game1.add_red(0,1)
game1.add_blue(1,4)
game1.render()
game1.is_under_attack()

# Diagonal Attack Case
game2 = ChessBoard()
game2.add_red(4,4)
game2.add_blue(2,2)
game2.render()
game2.is_under_attack()

# Horizantal Attack Case
game3 = ChessBoard()
game3.add_red(4,4)
game3.add_blue(4,2)
game3.render()
game3.is_under_attack()

# Vertical Attack Case
game4 = ChessBoard()
game4.add_red(4,2)
game4.add_blue(2,2)
game4.render()
game4.is_under_attack()
