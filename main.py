from pathfinding import Astar, BFS, DFS
from p5 import *
from taquin import Taquin

palette = {
        'background': (0, 0, 0),
        'borders': (100, 100, 100),
        'numbers': (210, 210, 210),
        'finished': (210, 20, 20)
        }
counter = -1
screen_size = (600, 600)
num = 3
tile_size = screen_size[0] // num


def draw_taquin(taquin: Taquin, finished: bool):
    for i in range(taquin.rows*taquin.cols):
        x = i % taquin.cols
        y = i//taquin.cols
        fill(*palette['borders'])
        rect(x*tile_size, y*tile_size, tile_size, tile_size)
        if taquin.data[i] == 0:
            s = ' '
        else:
            s = str(taquin.data[i])
        if finished:
            color = palette['finished']
        else:
            color = palette['numbers']
        fill(*color)
        text(s, 
             (
                 x*tile_size+tile_size//2,
                 y*tile_size+tile_size//2
              ))


def draw_path(path: [Taquin], fps=5):
    run(frame_rate=fps)


def setup():
    size(screen_size[0], screen_size[1])
    title('Taquin Solver')
    background(*palette['background'])
    f = create_font("Pixelfy.ttf", tile_size//2)
    text_font(f)
    text_align("CENTER", "CENTER")


def draw():
    global counter
    if counter < len(path)-1:
        counter += 1
        finished = False
    else:
        finished = True
        noLoop()
    draw_taquin(path[counter], finished)


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
    start = examples[2]
    assert len(final) == num**2, 'ERROR: Mismatched lengths'
    assert len(start) == num**2, 'ERROR: Mismatched lengths'
    firstState = Taquin(start, num)
    finalState = Taquin(final, num)
    global path
    path = DFS(firstState, finalState)
    # for state in path:
    #     state.print()
    draw_path(path)


if __name__ == '__main__':
    main()
