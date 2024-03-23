from taquin import Taquin


def Astar():
    pass


def DFS():
    pass


def BFS():
    pass


def main():
    game = Taquin()
    game.show()
    print('Reached final state:', game.check())
    s = int(input('swap: '))
    game.swap(s)
    game.show()


if __name__ == '__main__':
    main()
