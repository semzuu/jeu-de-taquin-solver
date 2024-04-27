from taquin import Taquin
from time import time


def Astar(FState: Taquin, LState: Taquin) -> list:
    start = time()
    visited = list()
    level = 0
    g = level
    h = LState - FState
    f = h + g
    Nvisited = [(FState, f, g)]
    parents = {FState: None}
    (currentState, f, g) = Nvisited.pop(0)
    stateCount = 1
    while not (currentState.compare(LState)):
        for state in currentState.transitions():
            if not (state.mcompare(visited)):
                g = level + 1
                h = LState - state
                f = h + g
                Nvisited.append((state, f, g))
                parents[state] = currentState
        visited.append(currentState)
        (currentState, f, g) = Nvisited.pop(0)
        stateCount += 1
        level = g + 1
    end = time()
    path = list()
    while True:
        path.insert(0, currentState)
        if parents[currentState] is None:
            break
        currentState = parents[currentState]
    return (path, visited, end-start, len(visited), stateCount)


def DFS(FState: Taquin, LState: Taquin, limit=None) -> tuple:
    start = time()
    if not limit:
        limit = float('inf')
    visited = list()
    Nvisited = [FState]
    parents = {FState: None}
    currentState = Nvisited.pop(0)
    level = 0
    stateCount = 1
    while not (currentState.compare(LState)) and level <= limit:
        for state in currentState.transitions():
            if not (state.mcompare(visited)):
                Nvisited.insert(0, state)
                parents[state] = currentState
        visited.append(currentState)
        currentState = Nvisited.pop(0)
        stateCount += 1
        level += 1
    end = time()
    path = list()
    while True:
        path.insert(0, currentState)
        if parents[currentState] is None:
            break
        currentState = parents[currentState]
    return (path, visited, end-start, len(visited), stateCount)


def BFS(FState: Taquin, LState: Taquin) -> list:
    start = time()
    visited = list()
    Nvisited = [FState]
    parents = {FState: None}
    currentState = Nvisited.pop(0)
    stateCount = 1
    while not (currentState.compare(LState)):
        for state in currentState.transitions():
            if not (state.mcompare(visited)):
                Nvisited.append(state)
                parents[state] = currentState
        visited.append(currentState)
        currentState = Nvisited.pop(0)
        stateCount += 1
    end = time()
    path = list()
    while True:
        path.insert(0, currentState)
        if parents[currentState] is None:
            break
        currentState = parents[currentState]
    return (path, visited, end-start, len(visited), stateCount)
