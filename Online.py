
import pygame
from network import Network

width=500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("client")

clientNumber = 0

class Player():
    def __init__(self, x, y, wid, hei, col):
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.col = col
        self.rect = (x,y,wid,hei)
        self.val = 3

    def draw(self, win):
        pygame.draw.rect(win, self.col, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.val
        if keys[pygame.K_RIGHT]:
            self.x += self.val
        if keys[pygame.K_UP]:
            self.y -= self.val
        if keys[pygame.K_DOWN]:
            self.y += self.val

        self.rect = (self.x, self.y, self.wid, self.hei)


def redrawWin(win, p):
    
    win.fill((255,255,255))
    p.draw(win)
    pygame.display.update()

def main():
    run = True
    p = Player(50,50,100,100,(0,255,255))
    clock = pygame.time.Clock()

    n = Network()

    startPos - n.get_pos()


    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWin(win, p)

main()