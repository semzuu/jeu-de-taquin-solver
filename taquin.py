import random


class Taquin:
    def __init__(self, data=None, num=3) -> None:
        self.rows = num
        self.cols = num
        self.data = [0]*self.rows*self.cols if data is None else data
        self.empty = self.data.index(0)

    def __repr__(self):
        return str(self.data)

    def __hash__(self):
        return hash(tuple(self.data))

    def randomize(self) -> None:
        '''
        Randomizes the board
        '''
        choices = [i for i in range(self.rows*self.cols)]
        for i in range(self.rows*self.cols):
            self.data[i] = random.choice(choices)
            choices.remove(self.data[i])
        self.empty = self.data.index(0)

    def copy(self) -> 'Taquin':
        '''
        Returns a copy of the board
        '''
        return Taquin(data=self.data.copy(), num=self.rows)

    def swap(self, posX: int, posY: int) -> None:
        '''
        Swaps the empty case with pos,
        if impossible, nothing will change
        '''
        pos = posY*self.cols+posX
        if self._neighbor(self.empty, pos):
            self.data[pos], self.data[self.empty] = self.data[self.empty], self.data[pos]
            self.empty = self.data.index(0)

    def moves(self) -> list:
        '''
        Returns a list of possible moves
        '''
        (emptyX, emptyY) = (self.empty % self.rows, self.empty // self.rows)
        moves = list()
        possible_moves = [
                (emptyX - 1, emptyY),  # left
                (emptyX + 1, emptyY),  # right
                (emptyX, emptyY - 1),  # up
                (emptyX, emptyY + 1)   # down
                ]
        for move in possible_moves:
            posX, posY = move
            if (0 <= posX <= self.cols-1) and (0 <= posY <= self.rows-1):
                moves.append(move)
        return moves

    def _neighbor(self, pos1, pos2) -> list:
        '''
        Checks if pos1 is neighbouring pos2
        '''
        return pos1 == pos2+1 or pos1 == pos2-1 or pos1 == pos2+self.rows or pos1 == pos2-self.rows

    def compare(self, TaquinB: 'Taquin') -> bool:
        '''
        Compare the board to another given board
        '''
        for i in range(len(self.data)):
            if self.data[i] != TaquinB.data[i]:
                return False
        return True

    def mcompare(self, Taquins: list('Taquin')) -> bool:
        '''
        Compare the board to a list of boards
        '''
        found = False
        for taquin in Taquins:
            if self.compare(taquin):
                found = True
        return found

    def show(self) -> None:
        '''
        Shows the board on screen
        '''
        print('='*8)
        for y in range(self.rows):
            print('-'+('-'*self.cols*2)+' \n|', end='')
            for x in range(self.cols):
                print(self.data[y*self.cols+x], end='|')
            print()
        print('-'+('-'*self.cols*2))
        print('='*8)

    def check(self) -> bool:
        '''
        Checks if the current board has reached the final state
        '''
        for y in range(self.rows):
            for x in range(self.cols):
                pos = y*self.rows+x
                if self.final[pos] != self.data[pos]:
                    return False
        return True

    def transitions(self) -> list:
        '''
        Returns a list of Successors
        '''
        transitions = list()
        possible_moves = self.moves()
        for move in possible_moves:
            x, y = move
            temp = self.copy()
            temp.swap(x, y)
            transitions.append(temp)
        return transitions
