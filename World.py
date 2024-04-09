from Cell import UCell

class UWorld:
    def __init__(self):
        self.Cells : list = list()

    def AddCell(self, X: int, Y: int):
        self.Cells.append(UCell(X, Y))

    def IsCellAlive(self, X: int, Y: int):
        return UCell(X, Y) in self.Cells

    def NextGeneration(self):
        NextGenerationCells: list = list()

        for Cell in self.Cells:
            AnyCellAlive = False

            if self.IsCellAlive(Cell.X - 1, Cell.Y - 1):
                AnyCellAlive = True
                break
            elif self.IsCellAlive(Cell.X, Cell.Y - 1):
                AnyCellAlive = True
                break
            elif self.IsCellAlive(Cell.X + 1, Cell.Y - 1):
                AnyCellAlive = True
                break
            elif self.IsCellAlive(Cell.X - 1, Cell.Y):
                AnyCellAlive = True
                break
            elif self.IsCellAlive(Cell.X + 1, Cell.Y):
                AnyCellAlive = True
                break
            elif self.IsCellAlive(Cell.X - 1, Cell.Y + 1):
                AnyCellAlive = True
                break
            elif self.IsCellAlive(Cell.X, Cell.Y + 1):
                AnyCellAlive = True
                break
            elif self.IsCellAlive(Cell.X + 1, Cell.Y + 1):
                AnyCellAlive = True
                break

        if AnyCellAlive:
            NextGenerationCells.append(Cell)

        self.Cells = NextGenerationCells