from taquin import Taquin


def Astar(FState: Taquin, LState: Taquin) -> list:
    '''
    f(node) = g(node) + h(node)
    g(node): niveau/nb de deplacement
    h(node): diff/nb de etats mal places
    Choose node based on score f(node)
    '''
    return


def DFS(FState: Taquin, LState: Taquin, limit=None) -> list:
    if not limit:
        limit = float('inf')
    visited = list()
    Nvisited = [FState]
    parents = {FState: None}
    currentState = Nvisited.pop(0)
    level = 0
    while not (currentState.compare(LState)) and level <= limit:
        for state in currentState.transitions():
            if not (state.mcompare(visited)):
                Nvisited.insert(0, state)
                parents[state] = currentState
        visited.append(currentState)
        currentState = Nvisited.pop(0)
        level += 1
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
