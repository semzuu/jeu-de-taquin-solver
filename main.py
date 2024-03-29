from taquin import Taquin


def Astar(FState: Taquin, LState: Taquin) -> list:
    return


def DFS(FState: Taquin, LState: Taquin, limit=None) -> list:
    visited = list()
    Nvisited = [FState]
    parents = {FState: None}
    currentState = Nvisited.pop(0)
    while not (currentState.compare(LState)):
        for state in currentState.transitions():
            if not (state.mcompare(visited)):
                Nvisited.insert(0, state)
                parents[state] = currentState
        visited.append(currentState)
        currentState = Nvisited.pop(0)
    path = list()
    while True:
        path.insert(0, currentState)
        if parents[currentState] is None:
            break
        currentState = parents[currentState]
    return path


def BFS(FState: Taquin, LState: Taquin) -> list:
    visited = list()
    Nvisited = [FState]
    parents = {FState: None}
    currentState = Nvisited.pop(0)
    while not (currentState.compare(LState)):
        for state in currentState.transitions():
            if not (state.mcompare(visited)):
                Nvisited.append(state)
                parents[state] = currentState
        visited.append(currentState)
        currentState = Nvisited.pop(0)
    path = list()
    while True:
        path.insert(0, currentState)
        if parents[currentState] is None:
            break
        currentState = parents[currentState]
    return path


def main():
    final = [
                1, 2, 3,
                8, 0, 4,
                7, 6, 5
            ]
    examples = [
            [1, 2, 3, 8, 6, 0, 7, 5, 4],
            [1, 2, 3, 8, 4, 0, 7, 6, 5],
            [1, 2, 3, 8, 6, 4, 7, 0, 5],
            [1, 2, 3, 8, 6, 4, 0, 7, 5]
            ]
    firstState = Taquin(examples[0])
    finalState = Taquin(final)
    path = DFS(firstState, finalState)
    for state in path:
        state.show()


if __name__ == '__main__':
    main()
