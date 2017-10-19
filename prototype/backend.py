nothing = " "

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
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.x, self.y))

    def __str__(self):
        return self.x.__str__() + ", " + self.y.__str__()

class Row:

    def __init__(self, row, board):
        self.row = row
        self.board = board
        self.owner = None

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

    def owned(self):
        if len(self.row) <= 0:
            return False
        if self.owner != None:
            return True
        player_index = self.row[0]
        for space in self.row:
            if space == nothing:
                return False
            if player_index != space:
                return False
            player_index = space
        self.owner = self.board.get_player(int(player_index))
        return True

    def get_owner(self):
        if not self.owned():
            return None
        return self.owner

    def __str__(self):
        return self.row.__str__()

class Player:

    def __init__(self, index):
        self.index = index
        self.rows = []
        self.points = 0

    def add_row(self, row):
        self.rows.append(row)

    def get_rows(self):
        return self.rows

    def get_row_count_length(self, length):
        num = 0
        for row in self.rows:
            if row.get_length() == length:
                num += 1
        return num

    def get_index(self):
        return self.index

    def contains(self, row):
        cont = False
        for e_row in rows:
            if e_row.contains(row):
                return True
        return False

    def __str__(self):
        return "Player " + self.index.__str__() + ", Rows: " + self.rows.__str__() +", Points: " + self.points.__str__()

def get_row(board, point, direc, length):
    x_offset = 1
    y_offset = 1
    if direc == 0 or direc == 4:
        x_offset = 0
    if direc == 3 or direc == 5:
        y_offset = -1
    if direc == 2 or direc == 6:
        y_offset = 0
    if direc == 5 or direc == 7:
        x_offset = -1

    point_list = []

    x = point.get_x()
    y = point.get_y()
    for i in range(length):
        point_list.append(board.get_at_space(x, y))
        x += x_offset
        y += y_offset
    return Row(point_list, board)

def check_board_state(board, player_list):
    num_players = len(player_list)

    for c in range(board.width):
        for r in range(board.height):
            for d in range(8):
                winning_row = get_row(board, Point(r, c), d, board.in_a_row)
                if winning_row.owned():
                    winning_row.get_owner().add_row(winning_row)
                    return winning_row.get_owner()
                for i in range(board.in_a_row-1, 0):
                    row = get_row(board, Point(r, c), d, i)
                    if row.owned():
                        owning_player = row.get_owner()
                        if not owning_player.contains(row):
                            owning_player.add_row(row)
