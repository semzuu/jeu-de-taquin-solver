import pygame


FONT = 'Pixelfy.ttf'


def initWindow(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Taquin Solver')
    return screen


class GRID:
    def __init__(self, taquin, x, y, tw, th, color, text_color, text_size=64):
        self.font = FONT
        self.x = x
        self.y = y
        self.tw = tw
        self.th = th
        self.color = color
        self.text_color = text_color
        self.text_size = text_size
        self.taquin = taquin

    def update(self, taquin):
        self.taquin = taquin

    def draw(self, screen):
        gridRect = pygame.Rect(self.x, self.y, self.tw*self.taquin.num, self.th*self.taquin.num)
        for i in range(self.taquin.num**2):
            tileX, tileY = (i % self.taquin.num, i // self.taquin.num)
            tileX, tileY = self.x+tileX*self.tw, self.y+tileY*self.th
            tileRect = pygame.Rect(tileX, tileY, self.tw, self.th)
            pygame.draw.rect(screen, self.color, tileRect)

            font = pygame.font.Font(self.font, self.text_size)
            text_surface = font.render(str(self.taquin.data[i]), True, self.text_color)
            text_x = tileX + (self.tw - text_surface.get_width()) // 2
            text_y = tileY + (self.th - text_surface.get_height()) // 2
            screen.blit(text_surface, (text_x, text_y))
        pygame.display.update(gridRect)


class BUTTON:
    def __init__(self, onclick, args, x, y, w, h, color, text, text_color, text_size=32):
        self.font = FONT
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.onclick = onclick
        self.args = args
        self.onclick_result = None

    def update(self, clicked):
        if clicked:
            mX, mY = pygame.mouse.get_pos()
            if (mX >= self.x) and (mX <= self.w + self.x) and (mY >= self.y) and (mY <= self.h + self.y):
                self.onclick_result = self.onclick.__call__(*self.args)

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, self.color, rect)

        font = pygame.font.Font(self.font, self.text_size)
        text_surface = font.render(self.text, True, self.text_color)
        text_x = self.x + (self.w - text_surface.get_width()) // 2
        text_y = self.y + (self.h - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))


class TEXT:
    def __init__(self, x, y, color, text, text_size=32):
        self.font = FONT
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.text_size = text_size

    def update(self, new_text):
        self.text = new_text

    def draw(self, screen):
        font = pygame.font.Font(self.font, self.text_size)
        text_surface = font.render(self.text, True, self.color)
        text_x = self.x
        text_y = self.y
        screen.blit(text_surface, (text_x, text_y))
