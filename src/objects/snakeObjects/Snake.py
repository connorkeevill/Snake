#CK

from objects.snakeObjects.Segment import Segment

class Snake():
    def __init__(self, column, row, board):
        self.column = column
        self.row = row
        self.direction = 'down'

        self.body = []
        self.spawn(board)

    def spawn(self, board):
        head = Segment(self.column, self.row)

        self.body.append(head)
        board[self.column][self.row].giveItem(head)
