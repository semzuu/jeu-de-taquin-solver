import random
def neighbor(pos1: int, pos2: int, row: int) -> bool:
    """
    Checks if pos1 is neighbouring pos2
    """
    return pos1 == pos2+1 or pos1 == pos2-1 or pos1 == pos2+row or pos1 == pos2-row
class Taquin:
    def __init__(self) -> None:
        self.rows = 3
        self.cols = 3
        self.data = [0]*self.rows*self.cols
        self.final = [
                1, 2, 3,
                8, 0, 4,
                7, 6, 5
                ]
        self.randomize()
        self.empty = self.data.index(0)
    def randomize(self) -> None:
        """
        Randomizes the board
        """
        choices = [i for i in range(self.rows*self.cols)]
        for i in range(self.rows*self.cols):
            self.data[i] = random.choice(choices)
            choices.remove(self.data[i])
    def swap(self, pos: int) -> None:
        """
        Swaps the empty case with pos,
        if impossible, nothing will change
        """
        pos-=1
        if neighbor(self.empty, pos, self.rows):
            self.data[pos], self.data[self.empty] = self.data[self.empty], self.data[pos]
            self.empty = self.data.index(0)
    def show(self) -> None:
        """
        Shows the board on screen
        """
        print('='*8)
        for y in range(self.rows):
            print(' ------\n|', end='')
            for x in range(self.cols):
                print(self.data[y*self.rows+x], end='|')
            print()
        print(' ------')
        print('='*8)
    
    def check(self) -> bool:
        """
        Checks if the current board has reached the final state
        """
        for y in range(self.rows):
            for x in range(self.cols):
                pos = y*self.rows+x
                if self.final[pos]!=self.data[pos]:
                    return False
        return True
