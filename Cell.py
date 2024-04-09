class UCell:
    def __init__(self, InitialX: int, InitialY: int):
        self.X = InitialX
        self.Y = InitialY

    def __eq__(self, __value: object) -> bool:
        return self.X == __value.X and self.Y == __value.Y