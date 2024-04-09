from World import *
import time
import os

if __name__ == '__main__':
    World : UWorld = UWorld()

    World.AddCell(1, 2)
    World.AddCell(2, 3)
    World.AddCell(3, 1)
    World.AddCell(3, 2)
    World.AddCell(3, 3)

    WorldGrid: list = list()
    while True:
        for X in range(10):
            for Y in range(10):
                if World.IsCellAlive(X, Y):
                    print(' X ', end='')
                else:
                    print('   ', end='')

            print('\n')
            
        World.NextGeneration()
        time.sleep(0.2)
        os.system('cls')