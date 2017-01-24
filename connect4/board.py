"""Comments

more comments
"""

class board:
    def __init__(self):
        self.cell = []
        for i in range(43):
            self.cell.append(0)
    
    def drop(self, column, player):
        for j in range(7):
            if self.cell[column+j*6] == 0:
                self.cell[column+j*6] = player
                return 0;
        return 1
    
    def display(self):
        for i in range(8):
            for j in range(7):
                print(self.cell[i+(6-j)*6])
            print("\n")
        return 0