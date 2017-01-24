"""Comments

more comments
"""

class board:
    def __init__(self):
        self.cell = []
        for i in range(42):
            self.cell.append(0)
    
    def drop(self, column, player):
        for j in range(7):
            if self.cell[column+j*6] == 0:
                self.cell[column+j*6] = player
                return 0;
        return 1
    
    def display(self):
        for i in range(6):
            printarray = []
            for j in range(7):
                printarray.append(self.cell[(5-i)*7+j])
            print(printarray)
        return 0