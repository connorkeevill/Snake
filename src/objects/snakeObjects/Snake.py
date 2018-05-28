#CK

from objects.snakeObjects.Segment import Segment

class Snake():
    def __init__(self, column, row, board):
        self.column = column
        self.row = row
        self.direction = 'down'

        self.body = []
        self.spawn(board)

    # | spawn()
    # |-----------------------------------------
    # | Creates the snake's "head" and places
    # | it into the board to begin the game
    # |---------------------------------
    def spawn(self, board):
        head = Segment(self.column, self.row)

        self.body.append(head)
        board[self.column][self.row].giveItem(head)
