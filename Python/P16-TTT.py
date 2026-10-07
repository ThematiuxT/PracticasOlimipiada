
from functools import wraps


class Player:
    def __init__(self, symbol:str):
        self.symbol = symbol

class Cell:
    def __init__(self, owner:Player):
        self.owner = owner
        self.occupied = False

    def show(self):
        return self.owner.symbol

    def setOwner(self, owner:Player):
        if self.occupied:
            return "Occupied"
        self.owner = owner
        self.occupied = True

class Board:
    def __init__(self):
        self.grid = []
        self.empty = Player(".")
        self.xTurn = True
        self.x = Player("X")
        self.o = Player("O")
        for y in range(3):
            self.grid.insert(y,[])
            for x in range(3):
                self.grid[y].insert(x,Cell(self.empty))
    
    def activeTurn(self):
        return self.x if self.xTurn else self.o

    def print(self):
        print("-0--1--2-")
        for y,row in enumerate(self.grid):
            for x,cell in enumerate(row):
                print(str("|"if x>0 else y)+cell.show(),end="|")
            print()
            print("---------")

    def checkState(self):
        for row in self.grid:
            if ((row[0].owner == row[1].owner)
                and (row[0].owner == row[2].owner)
                and (row[0].owner != self.empty)):
                return row[0].owner
        cols = []
        for x in range(3):
            cols.insert(x,[self.grid[0][x], self.grid[1][x], self.grid[2][x]])

        for col in cols:
            if ((col[0].owner == col[1].owner)
                and (col[0].owner == col[2].owner)
                and (col[0].owner != self.empty)):
                return col[0].owner

        diags = [
                    [
                        self.grid[0][0],
                        self.grid[1][1],
                        self.grid[2][2]
                    ],
                    [
                        self.grid[2][0],
                        self.grid[1][1],
                        self.grid[0][2]
                    ]
                ]

        for dia in diags:
            if ((dia[0].owner == dia[1].owner)
                and (dia[0].owner == dia[2].owner)
                and (dia[0].owner != self.empty)):
                return dia[0].owner       
        
        full = True
        for row in self.grid:
            for cell in row:
                full = full and (cell.owner != self.empty)

        if full:
            return self.empty
                    
                

    def turn(self):
        rt = None
        self.print()
        str_input = str(input())
        if len(str_input) < 2:
            print("Entrada incorrecta, ingresa coordenadas XY (e.j. 00, 21, 12)")
            return
        y = int(str_input[0])
        x = int(str_input[1])
        rt = rt or self.grid[y][x].setOwner(self.activeTurn())
        if rt:
            print(rt)
        else:
            self.xTurn = not self.xTurn


board = Board()
notDone = True

print("Ingresa coordenadas XY (e.j. 00, 21, 12)")
while notDone:
    win = board.turn()
    notDone = not board.checkState()
board.print()
winner = board.checkState().symbol
if winner != ".":
    print("Winner is", board.checkState().symbol)
else:
    print("Tied!")
