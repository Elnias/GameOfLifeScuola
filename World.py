from Cell import UCell

class UWorld:
    def __init__(self):
        self.Cells : list = list()

    def AddCell(self, X: int, Y: int):
        self.Cells.append(UCell(X, Y))

    def IsCellAlive(self, X: int, Y: int):
        return UCell(X, Y) in self.Cells

    def GetNumberOfAliveNeighbour(self, Cell: UCell) -> int:
        NumberOfCells = 0

        if UCell(Cell.X - 1, Cell.Y - 1) in self.Cells:
            NumberOfCells += 1
        
        if UCell(Cell.X, Cell.Y - 1) in self.Cells:
            NumberOfCells += 1
        
        if UCell(Cell.X + 1, Cell.Y - 1) in self.Cells:
            NumberOfCells += 1
        
        if UCell(Cell.X - 1, Cell.Y) in self.Cells:
            NumberOfCells += 1
        
        if UCell(Cell.X + 1, Cell.Y) in self.Cells:
            NumberOfCells += 1
        
        if UCell(Cell.X - 1, Cell.Y + 1) in self.Cells:
            NumberOfCells += 1
        
        if UCell(Cell.X, Cell.Y + 1) in self.Cells:
            NumberOfCells += 1
        
        if UCell(Cell.X + 1, Cell.Y + 1) in self.Cells:
            NumberOfCells += 1

        return NumberOfCells

    def NextGeneration(self):
        NextGenerationCells: list = list()

        DeadCells: list = list()

        for Cell in self.Cells:
            if not self.IsCellAlive(Cell.X - 1, Cell.Y - 1):
                DeadCells.append(UCell(Cell.X - 1, Cell.Y - 1))
            
            if not self.IsCellAlive(Cell.X, Cell.Y - 1):
                DeadCells.append(UCell(Cell.X, Cell.Y - 1))
            
            if not self.IsCellAlive(Cell.X + 1, Cell.Y - 1):
                DeadCells.append(UCell(Cell.X + 1, Cell.Y - 1))
            
            if not self.IsCellAlive(Cell.X - 1, Cell.Y):
                DeadCells.append(UCell(Cell.X - 1, Cell.Y))
            
            if not self.IsCellAlive(Cell.X + 1, Cell.Y):
                DeadCells.append(UCell(Cell.X + 1, Cell.Y))
            
            if not self.IsCellAlive(Cell.X - 1, Cell.Y + 1):
                DeadCells.append(UCell(Cell.X - 1, Cell.Y + 1))
            
            if not self.IsCellAlive(Cell.X, Cell.Y + 1):
                DeadCells.append(UCell(Cell.X, Cell.Y + 1))
            
            if not self.IsCellAlive(Cell.X + 1, Cell.Y + 1):
                DeadCells.append(UCell(Cell.X + 1, Cell.Y + 1))

        for Cell in DeadCells:
            if self.GetNumberOfAliveNeighbour(Cell) == 3:
                NextGenerationCells.append(Cell)

        for Cell in self.Cells:
            if self.GetNumberOfAliveNeighbour(Cell) in (2, 3):
                NextGenerationCells.append(Cell)

        self.Cells = NextGenerationCells