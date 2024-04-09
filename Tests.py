import unittest
import os
from World import UWorld

class GameOfLifeTests(unittest.TestCase):
    def test_OneCellAlive_CellDieInTheNextGeneration(self):
        World = UWorld()
        World.AddCell(0, 0)
        World.NextGeneration()

        self.assertFalse(World.IsCellAlive(0, 0))

    def test_OneCellAliveWithThreeNeighbour_CellSurvive(self):
        World = UWorld()
        World.AddCell(0, 0)
        World.AddCell(0, 1)
        World.AddCell(1, 0)
        World.AddCell(1, 1)

        World.NextGeneration()

        self.assertTrue(World.IsCellAlive(0, 0))

if __name__ == '__main__':
    os.system('clear')
    unittest.main()