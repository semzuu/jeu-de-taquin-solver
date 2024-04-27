from taquin import Taquin
from pathfinding import Astar, BFS, DFS
from gui import *


def hex_to_rgb(hex):
    assert hex[0] == '#' and len(hex) == 7, 'Invalid Hex'
    r, g, b = hex[1:3], hex[3:5], hex[5:7]
    return (int(r, 16), int(g, 16), int(b, 16))


PALETTE = {
        'background': hex_to_rgb('#222831'),
        'tiles': hex_to_rgb('#00ADB5'),
        'finished': hex_to_rgb('#008DDA'),
        'loading': hex_to_rgb('#393E46'),
        'text': hex_to_rgb('#EEEEEE'),
        'button': hex_to_rgb('#00ADB5')
        }


def main():
    examples = [
            [1, 2, 3, 8, 6, 0, 7, 5, 4],
            [1, 2, 3, 8, 4, 0, 7, 6, 5],
            [1, 2, 3, 8, 6, 4, 7, 0, 5],
            [1, 2, 3, 8, 6, 4, 0, 7, 5]
            ]
    final = [
                1, 2, 3,
                8, 0, 4,
                7, 6, 5
            ]
    start = examples[1]
    num = 3
    assert len(final) == num**2, 'ERROR: Mismatched lengths'
    assert len(start) == num**2, 'ERROR: Mismatched lengths'
    firstState = Taquin(start, num)
    finalState = Taquin(final, num)

    screen = initWindow(600, 600)
    clock = pygame.time.Clock()
    grid = GRID(
            firstState,
            10, 260, 100, 100,
            PALETTE['tiles'],
            PALETTE['text']
            )
    bfs = BUTTON(
            BFS, (firstState, finalState),
            10, 10, 100, 100,
            PALETTE['button'],
            'BFS',
            PALETTE['text']
            )
    dfs = BUTTON(
            DFS, (firstState, finalState),
            120, 10, 100, 100,
            PALETTE['button'],
            'DFS',
            PALETTE['text']
            )
    ldfs = BUTTON(
            DFS, (firstState, finalState, 2),
            230, 10, 100, 100,
            PALETTE['button'],
            'LDFS',
            PALETTE['text']
            )
    astar = BUTTON(
            Astar, (firstState, finalState),
            340, 10, 100, 100,
            PALETTE['button'],
            'A*',
            PALETTE['text']
            )
    executionTime = TEXT(
            10, 130,
            PALETTE['text'],
            'execution time: '
            )
    visitedCount = TEXT(
            10, 160,
            PALETTE['text'],
            'visited: '
            )
    generatedStates = TEXT(
            10, 190,
            PALETTE['text'],
            'generated: '
            )
    state = TEXT(
            10, 220,
            PALETTE['text'],
            'state: '
            )
    buttons = [bfs, dfs, ldfs, astar]
    text = [executionTime, visitedCount, generatedStates, state]
    clicked = False
    run = True
    fps = 1
    drawOrder, currentDraw, currentPath, path, visited = list(), None, None, None, None
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False
        screen.fill(PALETTE['background'])
        for button in buttons:
            button.update(clicked)
            if button.onclick_result is not None:
                (path, visited, executionTime, visitedCount, stateCount) = button.onclick_result
                drawOrder.append((visited, PALETTE['loading']))
                drawOrder.append((path, PALETTE['tiles']))
                text[0].update(f'execution time: {executionTime:.5f}')
                text[1].update(f'visited: {visitedCount}')
                text[2].update(f'generated: {stateCount}')
                button.onclick_result = None
            button.draw(screen)
        for item in text:
            item.draw(screen)

        if currentDraw is None and len(drawOrder) > 0:
            currentDraw = drawOrder.pop(0)
            currentPath, color = currentDraw
            if color == PALETTE['loading']:
                state.update('state: LOADING')
            elif color == PALETTE['tiles']:
                state.update('state: FINAL PATH')
            counter = 0

        if currentPath and counter < len(currentPath):
            if counter == len(currentPath)-1:
                grid.color = PALETTE['finished']
            else:
                grid.color = color
            grid.update(currentPath[counter])
            clock.tick(fps)
            counter += 1
        else:
            currentDraw = None
            currentPath = None
            color = (0, 0, 0)
            clock.tick(30)
            counter = 0

        grid.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
