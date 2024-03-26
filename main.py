from taquin import Taquin


def Astar(FState: Taquin, LState: Taquin) -> list:
    return


def DFS(FState: Taquin, LState: Taquin, limit=None) -> list:
    visited = list()
    Nvisited = [FState]
    currentState = Nvisited.pop(0)
    while currentState.compare(LState):
        for state in currentState.transitions():
            if state not in visited:
                Nvisited.insert(0, state)
        visited.append(currentState)
        currentState = Nvisited.pop(0)
    pass


def BFS(FState: Taquin, LState: Taquin) -> list:
    visited = list()
    Nvisited = [FState]
    currentState = Nvisited.pop(0)
    while currentState.compare(LState):
        for state in currentState.transitions():
            if state not in visited:
                Nvisited.append(state)
        visited.append(currentState)
        currentState = Nvisited.pop(0)
        pass


def main():
    final = [
                1, 2, 3,
                8, 0, 4,
                7, 6, 5
                ]
    firstState = Taquin()
    finalState = Taquin(final)
    firstState.randomize()
    firstState.show()
    print(firstState.moves())
    for state in firstState.transitions():
        state.show()


if __name__ == '__main__':
    main()
