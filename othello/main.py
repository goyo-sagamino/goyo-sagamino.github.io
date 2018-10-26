from tools import arrange
from objest import board, mark, tellb, put, action

board = board()
arrange(mark(board))

while True:
    text = input('x,y,color')

    x = int(text[0])
    y = int(text[2])
    color = text[4]


    board = put(board,x,y,color)
    #arrange(board)
    board = mark(action(board))
    arrange(board)
