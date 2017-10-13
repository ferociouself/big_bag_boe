from math import ceil
from backend import check_board_state
from backend import Player
class Board:

    nothing = " "

    highlight_begin = "\033[1;31m"
    highlight_end = "\033[0m"

    def __init__(self, width, height):
        self.board = [[self.nothing for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height
        self.players = [Player(x) for x in range(width-1)]
        self.in_a_row = int(ceil(height/2.0)) + 1

    def __str__(self):
        retStr = ""
        curRow = 0

        for row in self.board:
            rowStr = " | ".join(row)
            retStr += rowStr + "\n"
            curRow += 1
            if curRow < self.height:
                retStr += "-"*len(rowStr) + "\n"

        return retStr

    def place_in_space(self, place, spaceX, spaceY):
        if not self.board[spaceY][spaceX] == self.nothing:
            return False
        self.board[spaceY][spaceX] = place
        check_board_state(self, players)
        return True

    def get_player(self, index):
        return self.players[index]

    def get_at_space(self, spaceX, spaceY):
        return self.board[spaceY][spaceX]

    def highlight(self, str):
        return self.highlight_begin + str + self.highlight_end

    def highlight_row(self, val):
        retStr = ""
        curRow = 0

        for row in self.board:
            rowStr = " | ".join(row)
            retStr += rowStr + "\n"
            curRow += 1
            if curRow < self.height:
                if curRow - val == 1 or curRow - val == 0:
                    retStr += self.highlight("-"*len(rowStr)) + "\n"
                else:
                    retStr += "-"*len(rowStr) + "\n"

        return retStr

    def highlight_col(self, val):
        retStr = ""
        curRow = 0

        for row in self.board:
            rowStr = " | ".join(row[0:val])
            rowStr += self.highlight((" | " if not val == 0 else "") + row[val] + (" | " if not val == (len(row)-1) else ""))
            rowStr +=" | ".join(row[val+1:])
            rowLen = len(rowStr) - (len(self.highlight_begin) + len(self.highlight_end))
            retStr += rowStr + "\n"
            curRow += 1
            if curRow < self.height:
                retStr += "-"*rowLen + "\n"

        return retStr
