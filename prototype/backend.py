class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x && self.y == other.y
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.x, self.y))

class Row:

    def __init__(self, row):
        self.row = row

    def get_length(self):
        return len(self.row)

    def get_row(self):
        return self.row

    def contains(self, row):
        cont = True
        for elem in row:
            if not elem in self.row:
                cont = False
        return cont

class Player:

    def __init__(self, index):
        self.index = index
        self.rows = []
        self.points = 0

    def add_row(self, row):
        self.rows.append(row)

    def contains(self, row):
        cont = False
        for e_row in rows:
            if e_row.contains(row):
                return True
        return False

def check_board_state(board, player_list):
    num_players = len(player_list)

    for c in range(board.width):
        for r in range(board.height):
            for d in range(8):
                for i in range(board.in_a_row, 0):
                    for player in player_list:
                        
