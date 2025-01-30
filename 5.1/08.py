class Checkers:

    def __init__(self):
        self.field = [[Cell('X') for _ in range(8)] for _ in range(8)]
        for i in range(3):
            if i % 2 == 1:
                for j in range(0, 8, 2):
                    self.field[i][j] = Cell('B')
                    self.field[7 - i][j + 1] = Cell('W')
            else:
                for j in range(1, 8, 2):
                    self.field[i][j] = Cell('B')
                    self.field[7 - i][j - 1] = Cell('W')

    def get_cell(self, p):
        row = ord(p[0]) - ord('A')
        col = 8 - int(p[1])
        return self.field[col][row]

    def move(self, f, t):
        row = ord(f[0]) - ord('A')
        col = 8 - int(f[1])
        new_col = 8 - int(t[1])
        new_row = ord(t[0]) - ord('A')
        self.field[new_col][new_row] = self.field[col][row]
        self.field[col][row] = Cell('X')


class Cell:

    def __init__(self, status):
        self.stat = status

    def status(self):
        return self.stat
    

checkers = Checkers()
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()